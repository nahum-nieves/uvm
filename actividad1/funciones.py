"""
a) Declara una función add_two_numbers. Toma dos parámetros y devuelve una suma.
b) El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una
función que calcule el área_del_círculo.
c) Escribe una función llamada add_all_nums que tome un número arbitrario de
argumentos y los sume todos. Comprueba si todos los elementos de la lista son tipos
numéricos. Si no, dé una valoración razonable.
d) La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32.
Escribe una función que convierta °C a °F, convert_celsius_to-fahrenheit.
e) La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. Escribe una
función que calcule el conjunto de soluciones de una ecuación cuadrática,
solve_quadratic_eqn.
f) Declara una función llamada print_list. Toma una lista como parámetro e imprime cada
elemento de la lista.
g) Declara una función llamada lista_inversa. Toma una matriz como parámetro y
devuelve el reverso de la matriz (use bucles).
h) Declara una función add_two_numbers. Toma dos parámetros y devuelve una suma.
i) El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una
función que calcula el área_del_círculo.
j) Escribe una función llamada add_all_nums que tome un número arbitrario de
argumentos y los sume todos. Comprueba si todos los elementos de la lista son tipos
numéricos. Si no, dé una valoración razonable.
k) La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32.
Escribe una función que convierta °C a °F, convert_celsius_to-fahrenheit.
l) La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. Escribe una
función que calcule el conjunto de soluciones de una ecuación cuadrática,
solve_quadratic_eqn.
m) Declara una función llamada print_list. Toma una lista como parámetro e imprime cada
elemento de la lista.
n) Declara una función llamada lista_inversa. Toma una matriz como parámetro y
devuelve el reverso de la matriz (use bucles)."""
def add_two_numbers(a,b):
    return a+b

def area_del_circulo(r):
    return 3.141592*r*r

def add_all_nums(*args):
    suma = 0
    for number in args:
        if type(number) == int or type(number) == float:
            suma += number
        else:
            print(f"El elemento {number} no es un número")
    return suma

def convert_celsius_to_fahrenheit(c):
    return (c*9/5)+32

def solve_quadratic_eqn(a,b,c):
    x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    return x1, x2

def print_list(lista):
    for element in lista:
        print(element)

def lista_inversa(lista):
    lista_inversa = []
    for i in range(0,len(lista)):
        lista_inversa.append(lista[len(lista)-1-i])
    return
