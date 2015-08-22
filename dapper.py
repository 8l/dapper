# -*- coding: utf-8 -*-

import sys
import ethereum.opcodes as opcodes
import ethereum.abi as abi
from ethereum import utils
import struct


def to_bytes(long_int):
    bytes = []
    while long_int != 0:
        long_int, b = divmod(long_int, 256)
        bytes.insert(0, b)
    return bytes


class Dapper:
    stream = []
    frame = None
dapper = Dapper()

# Dynamically generate all mnemonic functions
for o in opcodes.opcodes:
    mnemonic = opcodes.opcodes[o][0].lower() + '_'
    ins = opcodes.opcodes[o][0]
    opcode = '%0.2x' % o

    code = '''
def {0}(*args):
    bytes = ['{1}'] + [format(x, '02x') for x in list(args)]
    dapper.stream += bytes
    '''.format(mnemonic, opcode)
    exec code in sys.modules[__name__].__dict__


class InstructionStream:

    def __enter__(self):
        dapper.frame = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(exc_type, exc_val, exc_tb)
        dapper.frame = None

    def __init__(self):
        pass


class Contract(InstructionStream):

    def function(self, label):
        return Function(self.translator.function_data[label])

    def __str__(self):
        return ''.join(dapper.stream)

    def __init__(self, _abi):
        self.translator = abi.ContractTranslator(_abi)
        # print(self.translator.function_data)


class Function(InstructionStream):
    def __init__(self, func_abi):
        self.signature = func_abi['signature']


def disasm(bytecode):
    op = None
    push_count = 0
    data = ''
    for i in xrange(0, len(bytecode), 2):
        word = int(bytecode[i:i+2], 16)
        if push_count > 0:
            data += str(word) + ', '
            push_count -= 1
        elif word in opcodes.opcodes:
            if op:
                yield('{0}_({1})'.format(op, data[:-2]))
            op = opcodes.opcodes[word][0].lower()
            data = ''
            if op.startswith('push'):
                push_count = int(op[4:])
    yield('{0}_({1})'.format(op, data[:-2]))


def signature():
    if hasattr(dapper.frame, 'signature'):
        return dapper.frame.signature
    else:
        raise Exception('No Function Signature found', dapper.frame)


# Macros
def push(word=None):
    if word == 0 and word is not None:
        result = [0]
    else:
        result = to_bytes(word)
    instruction = 'push{0}_'.format(len(result))
    try:
        getattr(sys.modules[__name__], instruction)(*result)
    except:
        msg = "{0}({1}) instruction does not exist".format(instruction, result)
        raise Exception(msg)


def label(label):
    return utils.decode_int(utils.sha3(label)[:4])
