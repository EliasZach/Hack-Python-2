"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):    
    result = []
    
    if s == [0]:
        return [0]
    
    i = 1
    while i <= len(s):
        if i % 2 == 0:
            result.append(i)
            i += 1
        else:
            result.append(str(i))
            i += 1     
    return result

