import sys
import math
import os

directory = "output_" + sys.argv[1].split("\\")[-1]
try:
    os.mkdir(directory)
except OSError as error:
    pass
        
inputFile = open(sys.argv[1], "rb")
bytE = inputFile.read()
inputFile.close()

if (int.from_bytes(bytE[0:4], "big") != 1095910230):
    print("Wrong anime, dummy!")
    exit()

if (len(sys.argv) > 2):
    injectFile = open(sys.argv[2], "rb")
    needlE = injectFile.read()
    injectFile.close()
    
    index = int(sys.argv[2].split("_")[1].split(".")[0]) - 1
    offset = int.from_bytes(bytE[(16 + (index * 8)):(16 + (index * 8) + 4)], "little")
    size = int.from_bytes(bytE[(16 + (index * 8) + 4):(16 + (index * 8) + 8)], "little")
    
    newFile = open("OUTPUT " + sys.argv[1].split("\\")[-1], "ab")
    newFile.write(bytE[0:offset])
    newFile.write(needlE[0:size])
    if (len(needlE) < size):
            newFile.write(bytes(size - len(needlE)))
    newFile.write(bytE[(offset + size):len(bytE)])
    newFile.close()
    exit()

numberOfFiles = int.from_bytes(bytE[4:8], "little")
skip = 0

for i in range(numberOfFiles):
    offset = int.from_bytes(bytE[(16 + (i * 8)):(16 + (i * 8) + 4)], "little")
    size = int.from_bytes(bytE[(16 + (i * 8) + 4):(16 + (i * 8) + 8)], "little")
    data = bytE[offset:(offset + size)]
    
    extension = ".bin"
    if (int.from_bytes(data[0:4], "big") == 1380401998):
        extension = ".NCGR"
    elif (int.from_bytes(data[0:4], "big") == 1380074318):
        extension = ".NCBR"
    elif (int.from_bytes(data[0:4], "big") == 1380729678):
        extension = ".NCLR"
    elif (int.from_bytes(data[0:4], "big") == 1380860238):
        extension = ".NANR"
    elif (int.from_bytes(data[0:4], "big") == 1380270926):
        extension = ".NCER"
    elif (int.from_bytes(data[0:4], "big") == 1380143950):
        extension = ".NSCR"
    elif (int.from_bytes(data[0:4], "big") == 1380011342):
        extension = ".NMAR"
    elif (int.from_bytes(data[0:4], "big") == 1380142414):
        extension = ".NMCR"
    elif (int.from_bytes(data[0:4], "big") == 1381254734):
        extension = ".NFTR"

    if (size < 1000000) and (offset > 0) and ((offset + size) < len(bytE)):
        newFile = open(directory + "/" + str(offset) + "_" + str(offset + size) + "__" + str(i + 1).zfill(4) + extension, "wb")
        newFile.write(data)
        newFile.close()
    else:
        skip = skip + 1

if (skip == 0):
    exit()

for i in range(skip):
    j = i + 1 + numberOfFiles
    
    offset = int.from_bytes(bytE[(16 + (j * 8)):(16 + (j * 8) + 4)], "little")
    size = int.from_bytes(bytE[(16 + (j * 8) + 4):(16 + (j * 8) + 8)], "little")
    data = bytE[offset:(offset + size)]
    
    extension = ".bin"
    if (int.from_bytes(data[0:4], "big") == 1380401998):
        extension = ".NCGR"
    elif (int.from_bytes(data[0:4], "big") == 1380074318):
        extension = ".NCBR"
    elif (int.from_bytes(data[0:4], "big") == 1380729678):
        extension = ".NCLR"
    elif (int.from_bytes(data[0:4], "big") == 1380860238):
        extension = ".NANR"
    elif (int.from_bytes(data[0:4], "big") == 1380270926):
        extension = ".NCER"
    elif (int.from_bytes(data[0:4], "big") == 1380143950):
        extension = ".NSCR"
    elif (int.from_bytes(data[0:4], "big") == 1380011342):
        extension = ".NMAR"
    elif (int.from_bytes(data[0:4], "big") == 1380142414):
        extension = ".NMCR"
    elif (int.from_bytes(data[0:4], "big") == 1381254734):
        extension = ".NFTR"

    if (size < 1000000) and (offset > 0) and ((offset + size) < len(bytE)):
        newFile = open(directory + "/" + str(offset) + "_" + str(offset + size) + "__" + str(j + 1).zfill(4) + extension, "wb")
        newFile.write(data)
        newFile.close()