import os

"""
Simulador de cajero automático:

Crea un programa que simule las operaciones básicas de un cajero automático. El programa debe permitir al usuario realizar operaciones como consultar saldo, retirar dinero y depositar dinero. Además, debe mantener un registro de las transacciones realizadas. 

"""

# INICIALIZAR VARIABLES
saldo = 0
registro_transacciones = []


# DEFINCION DE FUNCIONES
# Funcion que muestra el menu

def mostrar_menu():
    print('Bienvenidos al cajero.')
    print('1-Consultar saldo.')
    print('2-Retirar dinero.')
    print('3-Depositar dinero.')
    print('4-Mostrar movimientos')
    print('5-Salir')

def consultar_saldo():
    print(f'Saldo actual: {saldo}')


def retirar_dinero(importe):
    global saldo
    if importe <= saldo:
        saldo -= importe
        registro_transacciones.append(f'Retiro: {importe}')
        print("--------------------------------------------------------")
        print(f'Retiro exitoso. Le quedan {saldo} pesos')
        print("--------------------------------------------------------")
    else:
        print("--------------------------------------------------------")
        print(f"Saldo insuficiente. Usted tiene {saldo} pesos")
        print("--------------------------------------------------------")

def depositar_dinero(importe):
    global saldo
    saldo += importe
    registro_transacciones.append(f'Deposito: {importe}')
    print("--------------------------------------------------------")
    print(f'Deposito exitoso. Su saldo actual es {saldo} pesos')
    print("--------------------------------------------------------")


def mostrar_movimientos():
    print("Registro de transacciones.")
    for transaccion in registro_transacciones:
        print(transaccion)


while True:
    mostrar_menu()
    opcion = input('Ingrese una opcion: ')

    if not opcion.isdigit():
        os.system('clear')
        print("--------------------------------------------------------")
        print('Opcion no valida. Debe ingresar un numero.')
        print("--------------------------------------------------------")
        continue

    opcion = int(opcion)

    if opcion == 1:
        consultar_saldo()
    elif opcion == 2:
        importe = float(input('Ingrese el importe que desea retirar: '))
        os.system('clear')
        retirar_dinero(importe)
    elif opcion == 3:
        importe = float(input('Ingrese el importe que desea depositar: '))
        os.system('clear')
        depositar_dinero(importe)
    elif opcion == 4:
        os.system('clear')
        mostrar_movimientos()
    elif opcion == 5:
        os.system('clear')
        print("--------------------------------------------------------")
        print('Gracias por utilizar el cajero')
        print("--------------------------------------------------------")
        break
    else:
        os.system('clear')
        print("--------------------------------------------------------")
        print('Opcion invalida. Ingrese una opcion correcta.')
        print("--------------------------------------------------------")