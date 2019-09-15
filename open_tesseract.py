import argparse
import os

from directory_processing import process_directory
from file_processing import read_file


# TODO: Is Exception the best way forward??

def main():
    """
    Entry to tesseract program
    :return: None
    """

    print('Hello World')
    parse_command_line_arguments()


def processing(process_args):
    """
    Check validity of argument passed
    :return: None
    """
    print(process_args)
    if not os.path.exists(process_args):
        raise OSError
    if os.path.isfile(process_args):
        if process_args.split('.')[-1] in ['jpg', 'png', 'tiff', 'gif']:
            read_file(process_args)
        else:
            raise Exception('Not an image file')
    else:
        process_directory(process_args)


def parse_command_line_arguments():
    """
    Parse arguments from command line
    Direct to appropriate file
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help="Single File to be read")
    # parser.add_argument('-b', '--batch', help="Directory to batch process")
    args = parser.parse_args()
    processing(args.input)


if __name__ == '__main__':
    main()
