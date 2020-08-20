#coding: utf-8
from __main__ import *
from java.util import List
from ghidra.util import Msg

from ghidra.program.model.listing import FunctionManager
from ghidra.program.model.symbol import SourceType
from ghidra.app.cmd.function import ApplyFunctionSignatureCmd
from ghidra.program.util import FunctionUtility

print "Starting to sync"

f = askFile("Give me a file to open", "Go baby go!")

for line in file(f.absolutePath):  # note, cannot use open(), since that is in GhidraScript
    pieces = line.split()
    src_fn = pieces[0]
    dest = pieces[1]

    # find .._fn
    signature_fn = None
    address_dest = None
    # testi
    #src_funct = None

    try:
        fm = currentProgram.getFunctionManager()
        functions = fm.getFunctions(True)
        for f in functions:
            # print(f.getSignature().getPrototypeString())
            if src_fn == f.getName():
                print "source found:" + f.getName()
                signature_fn = f.getSignature()
                # testi
                #src_funct = f
                break
    except Exception as error:
        print "Error: " + repr(error)

    # find dest
    try:
        fm = currentProgram.getFunctionManager()
        functions = fm.getFunctions(True)
        for f in functions:
            # print(f.getSignature().getPrototypeString())
            if dest == f.getName():
                print "destination found:" + f.getName()
                address_dest = f.getEntryPoint()
                print "--> addr:" + address_dest.toString()
                typeForUserChange = SourceType.USER_DEFINED
                print "typeForUserChange:" + typeForUserChange.getDisplayString() 
                print "signature:" + signature_fn.getPrototypeString()

                print "ghidra ver:" + getGhidraVersion()
                break
    except Exception as error:
        print "Error: " + repr(error)
    
print "Finished with sync"