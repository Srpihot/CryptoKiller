#!/usr/bin/env python3
# usage: python3 ./baseN.py --help

import math
import argparse


def encode(text, encodeMap, encodingBit):
    binary = ''.join([format(x, '08b') for x in text.encode('utf8')])
    binary += (encodingBit - len(binary) % encodingBit) * '0'
    splittedArray = [binary[x:x + encodingBit] for x in range(0, len(binary), encodingBit)]
    encodedString = ''.join([encodeMap[int(x, 2)] for x in splittedArray])
    encodedString += (2 - len(encodedString) % 2) * '='
    return encodedString


def decode(text, encodeMap, encodingBit):
    text = text.replace('=', '')
    indexMap = [encodeMap.index(x) for x in text]
    binString = ''.join([format(x, f'0{encodingBit}b') for x in indexMap])
    binString += (8 - len(binString) % 8) * '0'
    binArray = [binString[x:x + 8] for x in range(0, len(binString), 8)]
    decodedString = bytes([int(x, 2) for x in binArray]).decode('utf8')
    return decodedString


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='source text')
    parser.add_argument('--map', type=argparse.FileType(), help='map file')
    parser.add_argument(
        '--decode', action='store_const', const=decode, default=encode, dest='function', help='decode mode')
    args = parser.parse_args()

    encodeMap = list(args.map.read())
    encodingBit = math.floor(math.log2(len(encodeMap)))
    print('Base' + str(2**encodingBit) + ' (mapsize: ' + str(len(encodeMap)) + ')')

    source = args.text
    print('source: ' + source)

    processed = args.function(source, encodeMap, encodingBit)
    print('target: ' + processed)
