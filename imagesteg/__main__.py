import argparse
import sys

from . import ui

from .imagesteg import Imagesteg


def blank_builder(parser):
    pass


def extract_bits(args):
    if args.infile is None:
        raise Exception()
    imagesteg = Imagesteg(args.infile)
    channel_map = {
        'r': imagesteg.RED,
        'g': imagesteg.GREEN,
        'b': imagesteg.BLUE,
    }
    pairs = list(map(lambda x: (channel_map[x[0]], int(x[1:])), args.bits.split(',')))
    res = imagesteg.extract_bits(pairs)
    sys.stdout.buffer.write(res)


def extract_bits_builder(parser):
    parser.add_argument('--bits', dest='bits', required=True)


def extract_bit_plane(args):
    if args.infile is None:
        raise Exception()
    imagesteg = Imagesteg(args.infile)
    channel_map = {
        'r': imagesteg.RED,
        'g': imagesteg.GREEN,
        'b': imagesteg.BLUE,
    }
    channel, nth = (channel_map[args.bit[0]], int(args.bit[1:]))
    new_im = imagesteg.extract_bit_plane(channel, nth)
    new_im.save(args.outfile, quality=100)


def extract_bit_plane_builder(parser):
    parser.add_argument('--bit', dest='bit', required=True)



def gray_bits(args):
    if args.infile is None:
        raise Exception()
    imagesteg = Imagesteg(args.infile)
    new_im = imagesteg.gray_bits()
    new_im.save(args.outfile, quality=100)


def inversion(args):
    if args.infile is None:
        raise Exception()
    imagesteg = Imagesteg(args.infile)
    new_im = imagesteg.invert()
    new_im.save(args.outfile, quality=100)


def _ui(args):
    if args.infile is None:
        raise Exception()
    ui.server.serve(args.infile)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

modules = [
    ('ui', _ui, blank_builder),
    ('inversion', inversion, blank_builder),
    ('gray_bits', gray_bits, blank_builder),
    ('extract_bits', extract_bits, extract_bits_builder),
    ('extract_bit_plane', extract_bit_plane, extract_bit_plane_builder),
]

for module_name, handler, builder in modules:
    subparser = subparsers.add_parser(module_name)
    subparser.set_defaults(handler=handler)
    builder(subparser)
    subparser.add_argument('infile', nargs='?', type=argparse.FileType('rb'), help='Input file.')
    subparser.add_argument('outfile', nargs='?', type=argparse.FileType('wb'), help='Output file. If blank, stdout is used.')


def main():
    args = parser.parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)


if __name__ == '__main__':
    main()
