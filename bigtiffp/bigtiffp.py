import sys
import struct
import argparse

BIGTIFF_VERSION = 43

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(
        description='Tests whether a .tiff file is of the bigtiff variety'
        epilog='Prints "yes" if file is bigtiff and "no" otherwise\n'
        'Exits with 0 if file is bigtiff and 1 otherwise\n'
        'Assumes that the given file is a .tiff and only checks whether '
        'bigtiff is enabled, no check to ensure file is .tiff is made.')

    argument_parser.add_argument('file', nargs=1,
                                 help='.tiff file to test for bigtiffness')

    args = argument_parser.parse_args()

    bigtiff_candidate_path = args.file[0]

    with open(bigtiff_candidate_path, 'rb') as f:
        bigtiff_mv = memoryview(f.read())
        endianness, version = struct.unpack('hh', bigtiff_mv[:4])

        message = 'no'
        exit_code = 1

        if version == BIGTIFF_VERSION:
            message = 'yes'
            exit_code = 0

        print(message)
        sys.exit(exit_code)
