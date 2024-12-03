# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
# ]
# ///

"""Port of genday.sh to Python, for ,e.g., those on Windows."""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

import requests

BASE_URL = "https://adventofcode.com/{year}/day/{day}"

FILE_TEMPLATE = """#!/usr/bin/env python3
# {url}

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

print(f"Part 1: {{}}")
print(f"Part 2: {{}}")"""


def parse_args():
    ap = argparse.ArgumentParser(description="Challenge helper for AOC.")
    ap.add_argument(
        "day",
        type=int,
        choices=range(1, 26),
        default=datetime.now().astimezone().day,
        nargs="?",
        metavar="day",
        help="Day to template. Uses current date if omitted. In range [1 - 25].",
    )
    ap.add_argument(
        "year",
        type=int,
        default=datetime.now().astimezone().year,
        nargs="?",
        help="Year to template (with day). Uses current year if omitted.",
    )
    ap.add_argument(
        "-s",
        "--session",
        type=str,
        required=False,
        help="Value of 'session' cookie on AOC site. Also checks the environment variable $AOC_SESSION. If both are set, this option takes precedence.",
    )
    ap.add_argument(
        "--input-only",
        action="store_true",
        required=False,
        help="Don't create a folder or script, only dump challenge input as 'dayXX.txt'.",
    )
    ap.add_argument("--force", action="store_true", required=False, help="Ignore sanity checks.")
    return ap.parse_args()


def main():
    args = parse_args()
    print(f"[-] Generating for {args.year} day {args.day:02d}")

    aoc_session = args.session or os.environ.get("AOC_SESSION")
    if not aoc_session:
        print("[!] $AOC_SESSION/--session is not set!")
        print(
            "    Set the $AOC_SESSION environment variable to the conent of the 'session' cookie on adventofcode.com."
        )
        print("    Or, pass it to this script with the --session flag.")
        sys.exit(1)

    # Check that script is run from correct directory, prevent unintended overwrites.
    if (Path.cwd().resolve() != Path(__file__).resolve().parent) and not args.force:
        print(
            "[!] Script is not being run from it's directory. "
            "As it uses relative paths, ensure you are running it from the correct directory. Use --force to ignore."
        )
        sys.exit(1)

    # Create structure for day
    gen_path = Path(f"day{args.day:02d}")
    try:
        # Create dayXX folder
        if not args.input_only:
            gen_path.mkdir(exist_ok=args.force)
    except FileExistsError:
        print(f"[!] Subdirectory '{gen_path}' already exists. If this is expected, try again with --force.")
        sys.exit(1)

    # Pull challenge input
    url = BASE_URL.format(year=args.year, day=args.day)
    resp = requests.get(
        url + "/input",
        cookies=requests.utils.cookiejar_from_dict({"session": aoc_session}),
        timeout=10,
    )
    resp.raise_for_status()

    input_path = (gen_path / Path("input.txt")) if not args.input_only else Path(f"day{args.day:02d}.txt")
    input_path.write_text(resp.text, "utf8")

    # Create dayXX/dayXX.py file
    if not args.input_only:
        script_path = gen_path / Path(f"day{args.day:02d}.py")
        if not args.force and script_path.exists():
            print(f"[!] File at path {script_path} already exists! Use --force to ignore.")
            sys.exit(1)
        script_path.write_text(FILE_TEMPLATE.format(url=url))

    print("[+] Complete!")


if __name__ == "__main__":
    main()
