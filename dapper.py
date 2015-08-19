# -*- coding: utf-8 -*-

import sys
import ethereum.opcodes as opcodes
import ethereum.abi as abi


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
    # TODO ins length check on args?
    bytes = ['{1}'] + ['%0.2x' % x for x in list(args)]
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

def signature():
    if hasattr(dapper.frame, 'signature'):
        return dapper.frame.signature
    else:
        raise Exception('No Function Signature found', dapper.frame)