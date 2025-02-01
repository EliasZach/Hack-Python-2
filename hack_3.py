"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""
def fn_hack_3(s):
    diccionario = {
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v'
    }
    traduccion = ''.join(diccionario.get(char, char) for char in s)
    char = False
    result = ''
    for i in traduccion:
        if i.isalpha() and not char:
            result += i.upper()
            char = True
        else:
            result += i
    if len(result) > 2:
        result = result[:-1] + result[-1].upper()
    return result
            
    

