"""
Verificar una contraseña
En este ejercicio escribirá una función que determina si una contraseña es buena o no. Definiremos como una buena contraseña aquella que tenga una longitud de al menos 8 caracteres y contenga al menos una letra mayúscula, al menos una letra minúscula y al menos un número. Su función debe devolver verdadero si la contraseña que se le pasó, como único parámetro, es buena, de lo contrario debería devolver falso. Incluya un programa principal que lea una contraseña del usuario e informe si es buena o no.
"""



def validar_minus(pwd):
    for letra in pwd:
        if letra.islower():
            return True

def validar_mayus(pwd):
    for letra in pwd:
        if letra.isupper():
            return True
        
def tiene_num(pwd):
    for letra in pwd:
        if letra.isdigit():
            return True

def tiene_longitud(pwd):
    if len(pwd) >= 8:
        return True




def valida_contrasenia(pwd):
    if validar_minus(pwd) and validar_mayus(pwd) and tiene_num(pwd) and tiene_longitud(pwd):
        return True
    else:
        return False
    

contra = input('Ingrese una contrasenia: ')

if valida_contrasenia(contra):
    print('Contra buena!!')
else:
    print('Contra mala!! Intente otra')
