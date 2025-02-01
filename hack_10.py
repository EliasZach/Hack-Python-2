"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    resultado = []
    mapeo = {
        'a': '1', 'b': '2',
        'c': '3', 'd': '4',
        'e': '5', 'f': '6'
    }
    for d in s:
        nuevo_diccionario = {}
        for clave, valor in d.items():
            nuevo_diccionario[mapeo[clave]] = mapeo[valor]   
        resultado.append(nuevo_diccionario)  
    return resultado