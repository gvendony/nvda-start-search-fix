# Start Search Fix for NVDA

[Magyar leírás](README.hu.md)

This NVDA add-on stops the Windows 11 Start menu search from reading the "All" filter tab instead of the search result.

## The problem

When you type in the Start menu search, NVDA starts reading the top result. It is then interrupted by something like "All, tab, selected, 1 of 3", so you do not hear the result.

## The cause

The search results are a web page hosted in WebView2. Each time the results are redrawn, the page fires a selection event on the top result and then another on the "All" filter tab. NVDA cancels speech and reports every selected object inside the results document, so the tab interrupts the result and the navigator object moves to the tab.

## What the add-on does

The add-on ignores selection events on filter tabs inside the search results document. Nothing else changes, and it does not modify any Windows files.

## Installation

1. Download the `.nvda-addon` file from the [Releases](https://github.com/gvendony/nvda-start-search-fix/releases) page.
2. Open the file and confirm the installation.
3. Restart NVDA.

## Compatibility

- Tested with NVDA 2026.3 on Windows 11 26H2, build 26300.9711.
- Minimum NVDA version: 2025.2. Versions older than 2026.3 have not been tested.

## Known limitations

- A filter tab is not announced if it becomes selected while focus stays in the search box.
- Moving to the filter tabs with the Tab key has not been tested. It should work because real focus changes are separate events.

## Building from source

Python 3 is required. Run `python build.py`. The add-on is created in the `dist` folder.

## License

GNU General Public License version 2. See [LICENSE](LICENSE).
