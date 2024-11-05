# auto-harvest

**auto-harvest** is a Python script that automates the bulk downloading of files based on URL patterns with customizable placeholders. It’s ideal for scenarios where you have URL patterns and wordlists to substitute into the URLs, allowing for systematic, automated file retrieval.

## Getting Started

To download this script, clone the repository:

```bash
git clone https://github.com/CloudyKhan/auto-harvest.git
cd auto-harvest
```

## Features

- Supports one or two placeholders (`FUZZ1` and `FUZZ2`) in URLs for pattern-based downloads.
- Allows downloading based on a single URL pattern or multiple URL patterns listed in a file.
- Saves downloaded files in a specified output directory.
- Customizable timeout for HTTP requests.

## Requirements

- **Python 3**
- **Requests library**: Install with `pip` if not already installed.
  ```bash
  pip install requests
  ```

## Usage

```bash
python3 auto-harvest.py [-u URL_PATTERN] [-o OUTPUT_DIR] [-t TIMEOUT] [-f1 FUZZ1_WORDLIST] [-f2 FUZZ2_WORDLIST] [--url-file URL_FILE]
```

### Options

- **`-u`, `--url-pattern`**: The base URL with `FUZZ1` and/or `FUZZ2` placeholders to specify where values from wordlists should be substituted.
- **`-o`, `--output-dir`**: The directory to save downloaded files. Defaults to `./downloaded_files` if not specified.
- **`-t`, `--timeout`**: Timeout for each HTTP request in seconds. Default is `10`.
- **`-f1`, `--fuzz1-wordlist`**: Wordlist file for `FUZZ1` placeholder.
- **`-f2`, `--fuzz2-wordlist`**: Wordlist file for `FUZZ2` placeholder.
- **`--url-file`**: File containing a list of URL patterns, each on a new line, to be processed.

## Examples

### Example 1: Download Files Using a Single URL Pattern and One Wordlist
Use a single URL pattern with one placeholder (`FUZZ1`) to download files.

```bash
python3 auto-harvest.py -u "http://example.com/docs/2020-FUZZ1.pdf" -f1 wordlist.txt -o ./my_downloads
```

In this example:
- `FUZZ1` in the URL pattern will be replaced by each entry in `wordlist.txt`.
- Files will be saved in the `./my_downloads` directory.

### Example 2: Download Files Using Two Placeholders and Two Wordlists
Use a URL pattern with both `FUZZ1` and `FUZZ2` placeholders for more complex substitutions.

```bash
python3 auto-harvest.py -u "http://example.com/docs/2020-FUZZ1-FUZZ2-report.pdf" -f1 months.txt -f2 days.txt -o ./reports
```

In this example:
- `FUZZ1` will be replaced by entries in `months.txt`.
- `FUZZ2` will be replaced by entries in `days.txt`.
- Files will be saved in the `./reports` directory.

### Example 3: Download Files Using Multiple URL Patterns from a File
Download files using several URL patterns listed in `patterns.txt`, each pattern containing `FUZZ1`.

```bash
python3 auto-harvest.py --url-file patterns.txt -f1 wordlist.txt -o ./batch_downloads
```

In this example:
- Each URL pattern in `patterns.txt` will have `FUZZ1` replaced by entries in `wordlist.txt`.
- Files will be saved in the `./batch_downloads` directory.

## Notes

- If only one wordlist is needed, you can omit the `-f2` argument, and `FUZZ2` will be ignored.
- The script will generate traffic proportional to the size of the wordlists. Consider limiting the size of wordlists to avoid high network traffic.
