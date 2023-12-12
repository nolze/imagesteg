from PIL import Image
from itertools import product
from bitstring import BitArray
import random


class Imagesteg:
    def __init__(self, fp):
        self.im = Image.open(fp)
        self.RED = 0
        self.GREEN = 1
        self.BLUE = 2
        self.ALPHA = 3

    def extract_bit_plane(self, channel, nth):
        new_im = Image.new("RGB", self.im.size)
        new_im_pxmap = new_im.load()
        w, h = self.im.size
        for i, j in product(range(w), range(h)):
            px = self.im.getpixel((i, j))
            pbit = ((px[channel] >> nth) & 1) * 0xff
            new_im_pxmap[i, j] = (pbit, pbit, pbit)
        return new_im

    def extract_channel_plane(self, channel):
        im = self.im
        new_im = Image.new("RGB", im.size)
        new_im_pxmap = new_im.load()
        w, h = im.size
        for i, j in product(range(w), range(h)):
            px = im.getpixel((i, j))
            new_px = [0, 0, 0, 0]
            new_px[channel] = px[channel]
            new_im_pxmap[i, j] = tuple(new_px)
        return new_im

    def invert(self):
        new_im = Image.eval(self.im, lambda x: x ^ 0xff)
        return new_im

    def gray_bits(self):
        im = self.im
        new_im = Image.new("RGB", im.size)
        new_im_pxmap = new_im.load()
        w, h = im.size
        for i, j in product(range(w), range(h)):
            px = im.getpixel((i, j))
            if px[0] == px[1] and px[1] == px[2]:
                new_im_pxmap[i, j] = (0xff, 0xff, 0xff)
            else:
                new_im_pxmap[i, j] = (0, 0, 0)
        return new_im

    def randomize_colormap(self, ratio=1):
        im = self.im
        new_im = Image.new("RGB", im.size)
        new_im_pxmap = new_im.load()
        new_colormap = {}
        w, h = im.size
        for i, j in product(range(w), range(h)):
            px = im.getpixel((i, j))
            rpx = tuple(map(lambda x: x//ratio, px))
            if rpx not in new_colormap:
                r = random.randrange(0x100)
                g = random.randrange(0x100)
                b = random.randrange(0x100)
                new_colormap[rpx] = (r, g, b)
            new_im_pxmap[i, j] = new_colormap[rpx]
        return new_im

    def extract_bits(self, pairs):
        bits = BitArray()
        w, h = self.im.size
        for j, i in product(range(h), range(w)):
            px = self.im.getpixel((i, j))
            for channel, nth in pairs:
                pbit = ((px[channel] >> nth) & 1)
                bits.append(bin(pbit))
        return bits.bytes
