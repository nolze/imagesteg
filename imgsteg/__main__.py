import argparse
import sys

from . import ui

from .imgsteg import Imgsteg


def blank_builder(parser):
    pass


def extract_bits(args):
    if args.infile is None:
        raise Exception()
    imgsteg = Imgsteg(args.infile)
    channel_map = {
        'r': imgsteg.RED,
        'g': imgsteg.GREEN,
        'b': imgsteg.BLUE,
    }
    pairs = list(map(lambda x: (channel_map[x[0]], int(x[1:])), args.bits.split(',')))
    res = imgsteg.extract_bits(pairs)
    sys.stdout.buffer.write(res)


def extract_bits_builder(parser):
    parser.add_argument('--bits', dest='bits', required=True)


def gray_bits(args):
    if args.infile is None:
        raise Exception()
    imgsteg = Imgsteg(args.infile)
    new_im = imgsteg.gray_bits()
    new_im.save(args.outfile, quality=100)


def inversion(args):
    if args.infile is None:
        raise Exception()
    imgsteg = Imgsteg(args.infile)
    new_im = imgsteg.invert()
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
