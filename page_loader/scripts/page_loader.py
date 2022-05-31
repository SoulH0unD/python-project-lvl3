#!/usr/bin/env python3
from page_loader.page_loader import download
from page_loader.lib.cli import cli


def main():
    args = cli()
    print(download(args.url, args.output))


if __name__ == "__main__":
    main()
