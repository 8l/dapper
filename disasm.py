from dapper import *

bytecode = "604380600b600039604e567c01000000000000000000000000000000000000000000000000000000006000350463eee9720681141560415760043560405260026040510260605260206060f35b505b6000f3"

contract = Contract([])

with contract:
    for instruction in disasm(bytecode):
        print(instruction)
        exec instruction

print(str(contract) == bytecode)
