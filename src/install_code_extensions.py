#!/usr/bin/env python3

import subprocess
from argparse import ArgumentParser


def parse_pargs():
    parser = ArgumentParser()
    parser.add_argument(
        "extensions", metavar="X", type=str, nargs="+", help="an extension identifier"
    )
    return parser.parse_args()


def install_code_extension(extension: str):
    subprocess.run(
        ["/usr/bin/code-server", "--install-extension", extension], check=True
    )


def main():
    args = parse_pargs()
    for ext in args.extensions:
        install_code_extension(ext)


if __name__ == "__main__":
    main()
