import argparse
import os


def cli():
    """Print diff between two files."""
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument('url', metavar='url', type=str)
    parser.add_argument('-o', '--output',
                        help='path to save the file',
                        default=os.getcwd())
    return parser.parse_args()
