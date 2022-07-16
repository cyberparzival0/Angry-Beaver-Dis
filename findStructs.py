#!//home/parzival/anaconda3/bin/python3

from re import findall, search

variableName = '[a-zA-Z]{1}[a-zA-Z0-9_]*'
alias = "typedef struct (%s) (%s)" % (variableName, variableName)
structNameAndAlias = "struct (%s)[^\}]*\}(\s*__attribute__\(\(packed\)\))?\s+(%s\s?,?\s?)" % (variableName, variableName)

def findTypes(data):
    _types = {}
    for match in findall(structNameAndAlias, data):
        _types[match[0]] = [item.split()[0] for item in match[1:] if len(item) > 0 and "__attribute__" not in item]

    for match in findall(alias, data):
        if match[0] not in _types.keys():
            _types[match[0]] = [match[1]]
        else:
            _types[match[0]].append(match[1])

    #print(_types.items())
    return _types.items()

if __name__ == "__main__":
    with open("structs.c") as _file:
        print(findTypes(_file.read()))
        
    with open("forLoop.py") as _file:
    	print(findTypes(_file.read()))
