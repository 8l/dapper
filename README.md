# Dapper

## A High-Level Assembly Meta-programmer in Python
### A spiritual successor to LLL and Serpent.

Every step in the Ethereum Virtual Machine costs GAS, and where modern Assemblers are used for speed gains (and masochism), there is an incredible economic benefit of hand-coding Smart Contracts.

At present, Dapper is in its infancy & is very low-level, but attempts to resolve this issue by using Python as a modern macro processor with the goal of walking a Python AST and generating EVM assembly.