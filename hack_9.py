"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    contador = 0
    nuevoDiccionario = {}
    for clave, valor in s.items():
        if contador == 0:
            valor_modificado = valor.replace('k', '')
            nuevoDiccionario = {clave.capitalize():valor_modificado.capitalize()}
            contador += 1
    return nuevoDiccionario
