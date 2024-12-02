# Template usage

Create a repository [from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template), using this repository (`sventec/aoc20XX`) as the selected template.

Each time you wish to try one of the day's challenges, do the following:

1. Set the `$AOC_SESSION` environment variable
1. Open the [aoc website](https://adventofcode.com/) and log in
1. Open Dev Tools (`F12`); navigate to _Storage_ (tab) -> _Cookies_ (sidebar) -> _`https://adventofcode.com`_
1. Copy the value of the `session` cookie
1. Set the env var - `export AOC_SESSION=53616c...`. Optionally, use `genday.py` with the `--session` argument instead.
1. Enter the `python` directory (`cd python`), ensure this is your CWD when running any genday script(s) for Python-based solutions
1. Generate a file structure and pull your challenge input using either `genday.sh` or `genday.py`
   - On Windows, it is likely only `genday.py` will work without additional setup

## `genday.sh`

- You must set the `AOC_SESSION` environment variable
- After doing so, run `source genday.sh <day> [<year>]`

### Example usage

- For day 2 of the current year: `source genday.sh 2`
- For day 11 of a previous year: `source genday.sh 11 2022`

## `genday.py`

### Requirements

- The `requests` library is required
  - Install it in a venv, globally (not recommended), or run the script with [uv](https://docs.astral.sh/uv/getting-started/installation/) (most convenient)

### Usage

- [uv](https://docs.astral.sh/uv/getting-started/installation/) makes it easy to create a temp venv, install `requests`, and run the script in one: `uv run genday.py ...`
- Or, manage `requests` yourself and run `python3 genday.py ...`
- This script has more control than the shell variant, explore with `python3 genday.py --help`
- Export the `AOC_SESSION` env var, _or_ set `-s`/`--session` to the cookie value

### Example usage

- For the current day of the current year: `python3 genday.py`
- For a previous day and/or previous year: `python3 genday.py 2`, `python3 genday.py 11 2022`
- To only save challenge input to `dayXX.txt` in the CWD: `python3 genday.py --input-only [day] [year]`

## Troubleshooting, etc.

The genday scripts, while in use on my personal devices, have not had extensive testing in other environments, etc. Open
an issue on the template repository to report any unexpected behavior, or for feature requests. PRs also welcome.

Support for languages other than Python may come in the future, based on personal use. Feel free to submit PRs for
language support as well.

---

**Below this point is the non-template README. After creating your own, delete from this line up.**

# Advent of Code 20XX Solutions

Advent of Code 20XX, in Python and possibly other languages

## Python

- [Day 1](./python/day01/day1.py)
- [Day X](./python/dayXX/dayX.py)
- ...
