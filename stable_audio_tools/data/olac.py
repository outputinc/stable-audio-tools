""" Tools to read and eventually write OLAC files. 
"""
import io
import struct
import numpy as np
import soundfile


OLAC_VERSION = 1
OLAC_XOR_KEY = ord('O')


class FormatException(Exception):
    """ Exception related to OLAC format parsing. 
    """
    pass


def olac2flac(b):
    """ Extract FLAC from OLAC wrapper. 
    """
    _b = bytearray(b)
    if _b[0:4] != b'OLAC':
        raise FormatException("Missing OLAC header")

    olac_version, reserved_size = struct.unpack('<xxxxIQ', _b[0:16])
    # if olac_version > OLAC_VERSION:
    #     raise FormatException("Unknown OLAC version")

    xor_flac = _b[16+reserved_size:]
    flac = bytearray([c^OLAC_XOR_KEY for c in xor_flac])

    return flac


def read(file):
    """ Read OLAC file at specified file path. 

    Returns:
        y: sample data for each channel (float)
        sr: sample rate (int)
    """
    b = olac2flac(file.read())
    fb = io.BytesIO(b)
    y, sr = soundfile.read(fb)
    return y, sr


if __name__ == "__main__":
    # test decoding
    import sys
    import math
    import sounddevice as sd
    import time

    with open(sys.argv[1], 'rb') as f:
        y, sr = read(f)
        soundfile.write('test.wav', y, sr)
        sd.play(y, sr)
        time.sleep(y.shape[0]/sr)
        sd.stop()
