'''
Name: Pham Gia Thong
Student's ID: 20120201
'''

from project import *
import os, fnmatch
import os.path as p
from pathlib import Path

def main():
    cur = p.dirname(Path(__file__).parent.absolute())
    ROOT_INPUT_FILENAME = cur + r'\\SCR\\INPUT\\input_'
    ROOT_OUTPUT_FILENAME = cur + r'\\SCR\\OUTPUT\\output_'
    numInputFile = len(fnmatch.filter(os.listdir(cur + '\\SCR\\INPUT\\'), '*.txt')) # count the amount of input file (txt)

    # Run all test cases
    for i in range(1,numInputFile + 1,1):
        readFileName = ROOT_INPUT_FILENAME + str(i) + ".txt"
        writeFileName = ROOT_OUTPUT_FILENAME + str(i) + ".txt"

        KB, alpha = Read_Data(readFileName)
        #read the empty file 
        if(len(KB) == 0 or len(alpha) == 0):
            return
        isEntailable, DataClauses = PL_Resolution(KB, alpha)
        Write_Data(writeFileName, DataClauses, isEntailable)
        #print out the result after resolving
        if isEntailable:
            print("Resolving input_" + str(i) + ".txt file successfully. The result is: " + "entail")
        else:
            print("Resolving input_" + str(i) + ".txt file successfully. The result is: " + "not entail")

# run main
if __name__ == '__main__':
    main()
