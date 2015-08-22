#!/usr/bin/python
# -*- coding: utf-8 -*-

from dapper import *

abi_signature = [{
    'type': 'function',
    'name': 'mul',
    'inputs': [{
        'name': 'x',
        'type': 'uint256'
    }, {
        'name': 'y',
        'type': 'uint256'
    }],
    'outputs': []
}]

contract = Contract(abi_signature)

# with contract.function('mul'):
#     x, y = signature()  # TODO make this return macro to get param

with contract:
    push1_(67)
    dup1_()  # duplicate 67 ?
    push1_(11)
    push1_(0)
    # 0 - start index in memory where the code is placed,
    # 1 - start index in the evm code
    # 2 - size of the code.
    codecopy_()  # 0, 11, 67,

    push1_(78)
    jump_()
    
    # (div (calldataload 0) 26959946667150639794667015087019630673637144422540572481103610249216)
    # (calldataload 0) gets code, and we divide by 2^224 to get first 32 bytes
    push29_(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    push1_(0)
    calldataload_()
    div_()  # i assume this adds result on stack

    push4_(238, 233, 114, 6)
    dup2_()  # we then duplicate the id and result?
    eq_()  # which then we perform operation, popping em off stack and pushing result
    iszero_()  # is item on stack 0?
    push1_(65) 
    jumpi_()  # conditionally sets program counter to 65 

    # (set 'x (calldataload 4))
    push1_(4)
    calldataload_()
    push1_(64)  # 64 is 'x', but why?
    mstore_()
    
    # (set '_temp_521 (mul (get 'x) 2))
    push1_(2)
    push1_(64)  # why 64 for 'x' ?
    mload_()  # load word from memory
    mul_()
    push1_(96)  # is '_temp_521
    mstore_()  # save to memory

    # (return (ref '_temp_521) 32)
    push1_(32)
    push1_(96)  # is '_temp_521
    return_()

    jumpdest_()  # valid destination for jump?
    pop_()

    jumpdest_()  # valid destination for jump?
    push1_(0)
    return_()


print(contract)
