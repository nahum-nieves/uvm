"""
Si el radio de un círculo es de 30 metros:
a) Calcula el área de un círculo y asigna el valor a una variable nombre de area_of_circle.
b) Calcula la circunferencia de un círculo y asigna el valor a una variable llamada
circum_of_circle.
c) Tome el radio como entrada del usuario y calcule el área.
"""
pi = 3.141592

# Tomar el radio como entrada del usuario
radio = float(input("Introduce el radio del círculo: "))

# Calcular el área del círculo
area_del_circulo = pi * (radio ** 2)
print(f"El área del círculo es: {area_del_circulo}")

# Calcular la circunferencia del círculo
circunferencia = 2 * pi * radio
print(f"La circunferencia del círculo es: {circunferencia}")