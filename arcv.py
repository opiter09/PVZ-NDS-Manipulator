import sys
import math
import os

directory = "output_" + sys.argv[2].split("\\")[-1].split(".")[0]
try:
    os.mkdir(directory)
except OSError as error:
    pass
        
inputFile = open(sys.argv[2], "rb")
bytE = inputFile.read()
inputFile.close()

if (int.from_bytes(bytE[0:4], "big") != 1095910230):
    print("Wrong anime, dummy!")
else:
    if (sys.argv[1] == "-r"):
        for root, dirs, files in os.walk(directory):
            for file in files:
                full = directory + "/" + file
                injectFile = open(full, "rb")
                needlE = injectFile.read()
                injectFile.close()
                
                index = int(full.split("_")[-1].split(".")[0]) - 1
                offset = int.from_bytes(bytE[(16 + (index * 8)):(16 + (index * 8) + 4)], "little")
                size = int.from_bytes(bytE[(16 + (index * 8) + 4):(16 + (index * 8) + 8)], "little")
                
                newFile = open("OUTPUT_" + sys.argv[2].split("\\")[-1], "wb")
                newFile.close()
                newFile = open("OUTPUT_" + sys.argv[2].split("\\")[-1], "ab")
                newFile.write(bytE[0:offset])
                newFile.write(needlE[0:size])
                if (len(needlE) < size):
                        newFile.write(bytes(size - len(needlE)))
                newFile.write(bytE[(offset + size):len(bytE)])
                newFile.close()
    elif (sys.argv[1] == "-u"):
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
                newFile = open(directory + "/" + str(offset).zfill(8) + "_" + str(offset + size) + "_" + str(i + 1).zfill(4) + extension, "wb")
                newFile.write(data)
                newFile.close()
            else:
                skip = skip + 1

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
                newFile = open(directory + "/" + str(offset).zfill(8) + "_" + str(offset + size) + "_" + str(j + 1).zfill(4) + extension, "wb")
                newFile.write(data)
                newFile.close()