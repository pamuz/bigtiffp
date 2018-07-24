import sys
import struct
import argparse

import sys
import struct
import argparse

BIGTIFF_VERSION = 43

def is_bigtiff(path):
    '''
    Returns True if the file at PATH is a .tiff with bigtiff enabled.
    Returns False otherwise.
    Assumes that the file at path is a .tiff file, which may or may
    not have bigtiff enabled. Does not check first to ensure that
    file is a .tiff
    '''
    with open(path, 'rb') as candidate_file:
        candidate_mv = memoryview(candidate_file.read())
        endianness, version = struct.unpack('hh', candidate_mv[:4])
        return version == BIGTIFF_VERSION
