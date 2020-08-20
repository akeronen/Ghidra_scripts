#Imports a file with lines in the form "symbolName 0xADDRESS"
#@category Data
#@author 

f = askFile("Give me a file to open", "Go baby go!")

for line in file(f.absolutePath):  # note, cannot use open(), since that is in GhidraScript
    pieces = line.split()
    address = toAddr(long(pieces[1], 16))
    retVal = disassemble(address)
    if(retVal):
        createFunction(address, pieces[0])