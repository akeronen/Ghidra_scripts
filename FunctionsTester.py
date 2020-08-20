#coding: utf-8
from __main__ import *
from java.util import List
from ghidra.util import Msg

from ghidra.program.model.listing import FunctionManager
from ghidra.program.model.symbol import SourceType
from ghidra.app.cmd.function import ApplyFunctionSignatureCmd
from ghidra.program.util import FunctionUtility

print "Starting funct tester"

# testi:
# b8048524 T sound_handle_timer

# Get address from String
address = currentProgram.getAddressFactory().getAddress("0xb8048524")

# Get the FunctionManager
fm = currentProgram.getFunctionManager()

# Get a function at a certain address
f = fm.getFunctionAt(address)
print "function at address:" + f.getName()
    
print "Finished funct tester"

# output:
#  FunctionsTester.py> Running...
#  Starting funct tester
#  function at address:sound_handle_timer
#  Finished funct tester
#  FunctionsTester.py> Finished!