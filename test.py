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
    dup1_()
    push1_(11)
    push1_(0)
    codecopy_()
    push1_(78)
    jump_()
    push29_(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    push1_(0)
    calldataload_()
    div_()
    push4_(238, 233, 114, 6)
    dup2_()
    eq_()
    iszero_()
    push1_(65)
    jumpi_()
    push1_(4)
    calldataload_()
    push1_(64)
    mstore_()
    push1_(2)
    push1_(64)
    mload_()
    mul_()
    push1_(96)
    mstore_()
    push1_(32)
    push1_(96)
    return_()
    jumpdest_()
    pop_()
    jumpdest_()
    push1_(0)
    return_()


print(contract)
