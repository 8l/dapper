# Dapper

## A High-Level Assembly Meta-programmer in Python
### A spiritual successor to LLL and Serpent.

Every step in the Ethereum Virtual Machine costs GAS, and where modern Assemblers are used for speed gains (and masochism), there is an incredible economic benefit of hand-coding Smart Contracts.

At present, Dapper is in its infancy & is very low-level, but attempts to resolve this issue by using Python as a modern macro processor with the goal of walking a Python AST and generating EVM assembly.

Check out [test.py](https://github.com/syng-io/dapper/blob/master/test.py) for a short example.

## Available Macros

#### push(int)
Shorthand for push1_(), push2_(), ...
Handles large ints and hex and converts them into appropriate push instruction

#### label(str): int
Returns int for [ABI Function Selector](https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI#function-selector)

## What else?

Theres a disassembler as well, see [disasm.py](https://github.com/syng-io/dapper/blob/master/disasm.py) for a short demo