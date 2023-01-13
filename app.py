def main():
    opciones = ["Salir", "SUMA", "RESTA", "MULTIPLICACION", "DIVISION", "RAIZ", "EXPONENTE", "SENO", "COSENO", "TANGENTE"]
    opcion = menu()

    while opcion != "0":
        print("Bienvenido a la operación %s" %opciones[int(opcion)])
        if opcion == "1":
            suma()
        if opcion == "2":
            resta()
        if opcion == "3":
            multi()
        if opcion == "4":
            division()
        if opcion == "5":
            raiz()
        if opcion == "6":
            exp()
        if opcion == "7":
            sen()
        if opcion == "8":
            cos()
        if opcion == "9":
            tan()
        opcion = menu()

    print("Saliendo...")


def menu():
    respuesta = input("""Bienvenido a Calculadora
    Seleccione una de las siguientes opciones:
    1.- Sumar
    2.- Restar
    3.- Multiplicar
    4.- Dividir
    5.- Raiz n
    6.- Exponente n
    7.- Seno
    8.- Coseno
    9.- Tangente
    0.- Salir  
    """ )
    return respuesta

def suma():
    a = input('Ingresa el primer valor: \n ')
    b = input('Ingresa el segundo valor: \n')
    print( 'El resultado es:')
    print(int(a) + int(b) )

def resta():
    a = input('Ingresa el primer valor: \n ')
    b = input('Ingresa el segundo valor: \n')
    print( 'El resultado es:')
    print(int(a) - int(b) )

def multi():
    a = input('Ingresa el primer valor: \n ')
    b = input('Ingresa el segundo valor: \n')
    print( 'El resultado es:')
    print(int(a) * int(b) )

def division():
    a = input('Ingresa el primer valor: \n ')
    b = input('Ingresa el segundo valor: \n')
    print( 'El resultado es:')
    print(int(a) / int(b) )

if __name__ == '__main__':
        main()