#!/usr/bin/env python
"""
A command-line tool for spliting POV-Ray density file (DF3)
to a series of separate images.

"""

from __future__ import print_function
import sys
import argparse
import struct

from PIL import Image


def from_big_endian(bytestring):
    """ Convert big-endian bytestring to int """
    bytestring = bytestring.rjust(4, b'\x00')
    return struct.unpack(">L", bytestring)[0]


def split_by_n(seq, chunk_size):
    """ Generator splitting a sequence into chunks """
    while seq:
        yield seq[:chunk_size]
        seq = seq[chunk_size:]


def df3split(filename, prefix="layer", img_format='tga', silent=True):
    """
    Split POV-Ray density file (DF3) to a series of separate images.

    :param filename: path to DF3 file to process
    :param prefix: output files prefix
    :param img_format: output files format (tga, png, etc.)
    :param silent: suppress output (info messages, progress etc.)

    """
    with open(filename, "rb") as f:
        # detect size
        header = f.read(6)
        x, y, z = [from_big_endian(v) for v in split_by_n(header, 2)]
        if not silent:
            print("Size: %dx%d, %d layers" % (x, y, z))

        # detect byte width
        data = f.read()
        byte_width = int(float(len(data)) / (x * y * z))
        if not silent:
            plural = ' s'[byte_width > 1]
            print("Voxel resolution: %d byte%s" % (byte_width, plural))

        # parse data and save images
        for img_num, img_data in enumerate(split_by_n(data, x * y)):
            values = split_by_n(img_data, byte_width)
            pixels = [from_big_endian(v) for v in values]
            layer_num = str(img_num).zfill(len(str(z)))
            img = Image.new("L", (x, y))
            img.putdata(pixels)
            img.save("%s%s.%s" % (prefix, layer_num, img_format.lower()))
            percentage = float(img_num + 1) / z * 100
            if not silent:
                sys.stdout.write("Processing data [%.2f%%]\r" % percentage)
                sys.stdout.flush()

        if not silent:
            print("\nDone.")


def main():
    """ Main script execution """
    parser = argparse.ArgumentParser(description="""
    Split POV-Ray density file (DF3) to a series of separate images
    """)
    parser.add_argument("df3file", help="DF3 filename, including path")
    parser.add_argument("-t", "--format", type=str,
                        choices=["tga", "png"],
                        default="tga",
                        help="Output files format")
    parser.add_argument("-p", "--prefix", type=str,
                        default="layer",
                        help="Output files prefix")
    parser.add_argument("-s", "--silent", help="Suppress output",
                        default=False, action="store_true")

    args = parser.parse_args()

    df3split(args.df3file, args.prefix, args.format, args.silent)


if __name__ == "__main__":
    main()
