#!/home/parzival/anaconda3/bin/python3

import re
import sys
from findStructs import findTypes

class Patterns:
    # Need to add struct
    def __init__(self, filename, lang = "Python"):
        self.filename = filename
        self.lang = lang
        with open(filename, 'r') as _file:
            self.file = _file.read()

        self.cTypes = "(" + "|".join([_type for _type in """_Bool char wchar_t char unsigned short unsigned int unsigned long unsigned long unsigned size_t ssize_t float double long char* wchar_t* void* void""".split()])
        if self.lang == "C":
            for _dict in findTypes(self.file):
                for key, vals in _dict.items():
                    self.cTypes += "|" + key
                    for val in vals:
                        self.cTypes += "|" + val
        self.cTypes += ")"

        self.file = self.file.split("\n")


        self.variableName = '[a-zA-Z]{1}[a-zA-Z0-9_]*'

        self.pyFunctionSignature = "^def %s(.*)( -> .*)?:" % (self.variableName)
        self.cFunctionSignature = "^[ ]*%s[ ]+%s(.*)"  % (self.cTypes, self.variableName)
        
        self.functionSignature = self.pyFunctionSignature if lang == "Python" else self.cFunctionSignature
    
    def cleanSignature(self, item, idx):
        item = item.strip()
        looking = True
        while looking:
            if item.find("  ") == True:
                item.replace("  ", " ")
            else:
                looking = False
         
        args = item[item.find('(') + 1: item.find(')')]
        line = item.split()
        final = {'args': None, 'start': idx}

        final['funcName'] = line[1][:line[1].find('(')] # not (

        if self.lang == "Python":
            if len(args):
                final['args'] = [[_arg.split()[1], _arg.split()[0][:-1]] for _arg in args.split(',')]
            if line[-1][-1] == ":":
                final['returnType'] = line[-1][:-1]
            else:
                final['returnType'] = line[-1]

        elif self.lang == "C":
            final['returnType'] = line[0]
            if len(args):
                final['args'] = [[_arg.split()[0], _arg.split()[1]] for _arg in args.split(',')]

        return final

    def extractSignatures(self) -> list:
        found = []
        appendEnd = False

        for idx, line in enumerate(self.file):
            match = re.search(self.functionSignature, line.strip())
            if match != None:
                found.append(self.cleanSignature(match.group(), idx))
                appendEnd = True
            else:
                if (line == "" or line == "}") and len(found) and appendEnd:
                    found[-1]['end'] = idx
                    appendEnd = False
        
        # Check if EOF when end of function
        if 'end' not in found[-1].keys():
            found[-1]['end'] = len(readFile) - 1
       
        #found["logic"] = self.findLogic()
        for idx in range(len(found)):
            
            found[idx]["logic"] = ""
            for _idx in range(found[idx]['start'] + 1, found[idx]['end']):
                found[idx]["logic"] += self.file[_idx]

        return found

    def findLogic(self) -> list:
        for functionSignature in self.extractSignatures():
            if functionSignature['funcName'] != "main":
                print(functionSignature)
                for idx in range(functionSignature['start']+1, functionSignature['end']):
                    print(self.file[idx])

if __name__ == "__main__":
    finding = Patterns(sys.argv[1], lang = sys.argv[2])
    print(finding.extractSignatures())
