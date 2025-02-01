"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""

def fn_hack_6(s):
    if not s:
        return ["0"]
    
    result = []
    
    for i in range(1, len(s) + 1):
        if i % 2 == 0:
            result.append("-")
        else:
            result.append(str(i))
    
    return result
