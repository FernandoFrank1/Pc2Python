# Estructuras Iterativas:

# Problema 1:

"""Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos). """

for numero in range(1500, 2701):
    
    if numero % 7 == 0 and numero % 5 == 0:
        print(numero)


# Problema 2:

"""Escriba un programa en Python para construir el siguiente patrón.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*                     """

numero_filas = 5

for i in range(numero_filas):
    print('* ' * (i + 1))


for i in range(numero_filas - 1, 0, -1):
    print('* ' * i)


# Problema 3:
"""Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.

Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.

Ejemplo:
“Desea ingresar un número?”: SI
“Ingrese el número:” 5
“¿Desea ingresar un número?”: SI
“Ingrese el número: ” 7
……
“Desea ingresar un número?”: NO

Números ingresados: [ 5,7, 6, 7, 8, 9, 1, 2, 3, 4]
Cantidad de números pares: 5
Cantidad de números impares: 4 """

numeros = []
pares = 0
impares = 0

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    elif respuesta == "NO":
        break
    else:
        print("Por favor, responda SI o NO.")

print(f'Números ingresados: {numeros}')
print(f'Cantidad de números pares: {pares}')
print(f'Cantidad de números impares: {impares}')


#Problema 4:
"""Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.

Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}

Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos. """


def ingresar_alumnos(numero_alumnos):
    lista_alumnos = []
    for i in range(numero_alumnos):
        alumno = {}
        alumno["Alumno"] = input(f"Ingrese el nombre del alumno {i+1}: ")
        alumno["Notas"] = []
        for j in range(3):
            nota = float(input(f"Ingrese la nota {j+1} del alumno {alumno['Alumno']}: "))
            alumno["Notas"].append(nota)
        lista_alumnos.append(alumno)
    return lista_alumnos

def mostrar_listado_alumnos(lista_alumnos):
    print("\nListado de Alumnos:")
    for alumno in lista_alumnos:
        print(f"Alumno: {alumno['Alumno']}")
        print(f"Notas: {alumno['Notas']}")
numero_alumnos = int(input("Ingrese el número de alumnos: "))
alumnos = ingresar_alumnos(numero_alumnos)

mostrar_listado_alumnos(alumnos)


# Funciones:

# Problema 5:

"""Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
Ejemplo:
Número ingresado: 15789000 y Dígito: 0
Cantidad de veces 0 en el número: 4

Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método
count. """

def contar_digitos(numero, digito):
    numero_str = str(numero)
    cantidad = numero_str.count(str(digito))
    return cantidad

numero_ingresado = int(input("Ingrese un número: "))
digito = int(input("Ingrese un dígito: "))

cantidad = contar_digitos(numero_ingresado, digito)

print(f"La cantidad de veces que aparece {digito} en el número {numero_ingresado} es: {cantidad}")


# Problema 6:

"""Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores."""

def serie_fibonacci(n):
    fib_serie = [0, 1]

    while fib_serie[-1] < n:
        fib_serie.append(fib_serie[-1] + fib_serie[-2])
    return fib_serie[:-1]

fib_serie_50 = serie_fibonacci(50)
print("La serie de Fibonacci entre 0 y 50 es:", fib_serie_50)


# Problema 7:

"""Escriba una función de Python que tome un número como parámetro y verifique que el número sea
primo o no. """

def evaluar_primo(numero):
    if numero <= 1:
        return False
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    return es_primo

numero = int(input('Ingrese un número: '))
es_primo = evaluar_primo(numero)

if es_primo:
    print(f'El número {numero} es primo')
else:
    print(f'El número {numero} no es primo')


# Problema 8:

"""Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento."""

def factorial(numero):
    if numero < 0:
        return
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

numero = int(input('Ingrese un número entero positivo: '))
print(f'El factorial de {numero} es: {factorial(numero)}')


# Métodos de Cadenas:

# Problema 9:

"""Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.

Ejemplo:
- Input: Twitter Output: Twttr
- Input: What's your name? Output: Wht's yr nm?"""

def omitir_vocales(cadena):
    vocales = 'aeiouAEIOU'
    nueva_cadena = ''
    for caracter in cadena:
        if caracter not in vocales:
            nueva_cadena += caracter
    return nueva_cadena

texto = input("Ingrese una cadena de texto: ")
resultado = omitir_vocales(texto)
print("Texto con vocales omitidas:", resultado)


# Problema 10:

"""En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de
1636!
Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
la lista abajo:
[
"Enero",
"Febrero",
"Marzo",
"Abril",
"Mayo",
"Junio",
"Julio",
"Agosto",
"Septiembre",
"Octubre",
"Noviembre",
"Diciembre"
]
Luego, genere esa misma fecha en formato AAAA-MM-DD.
Ejemplos:
- Input: 9/8/1636 | Output: 1636-09-08
- Input: Septiembre 8, 1636 | Output: 1636-09-08
- Input: 1/1/1970 | Output: 1970-01-01 """

def obtener_mes(mes):
    meses = [
        "enero",
        "febrero",
        "marzo",
        "abril",
        "mayo",
        "junio",
        "julio",
        "agosto",
        "septiembre",
        "octubre",
        "noviembre",
        "diciembre"
    ]
    return meses.index(mes.lower()) + 1


def convertir_fecha(input_fecha):
    partes_fecha = input_fecha.split()
    if "/" in partes_fecha[0]:
        mes, dia, anio = map(int, partes_fecha[0].split("/"))
    else:
        mes = obtener_mes(partes_fecha[0])
        dia = int(partes_fecha[1][:-1])
        anio = int(partes_fecha[2])
    return f"{anio:04d}-{mes:02d}-{dia:02d}"


input_fecha = input("Ingrese una fecha (en formato Mes/Día/Año o con el nombre del mes día, año): ")
fecha_formateada = convertir_fecha(input_fecha)
print("La fecha en formato AAAA-MM-DD:", fecha_formateada)
