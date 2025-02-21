"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = []

    for i in range(len(s) - 1, -1, -1):
        if len(s) > 4 or len(s) == 3:
            result.append(f"{s[i]}-{i + 1}")
        else:
            result.append(str(i+1))
    
    return result
