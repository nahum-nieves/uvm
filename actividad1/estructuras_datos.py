"""
a) Crea un diccionario vacío llamado perro.
b) Agrega nombre, color, raza, patas y edad al diccionario de perros.
c) Crea un diccionario de estudiantes y agregue nombre, apellido, sexo, edad, estado civil,
habilidades, país, ciudad y dirección como claves para el diccionario.
d) Obtén la longitud del diccionario del estudiante.
e) Obtén el valor de las habilidades y verifica el tipo de datos, debería ser una lista.
f) Modifica los valores de las habilidades agregando una o dos habilidades.
g) Obtén las claves del diccionario como una lista.
h) Obtén los valores del diccionario como una lista.
i) Cambia el diccionario a una lista de tuplas usando el método items().
j) Elimina uno de los elementos del diccionario.
k) Elimina uno de los diccionarios
"""
perro = dict()
perro['nombre'] = 'Mayka'
perro['color'] = 'Blanco'
perro['raza'] = 'Bishon'
perro['patas'] = 4
perro['edad'] = 13
estudiantes = dict()
estudiantes['nombre'] = 'Arturo'
estudiantes['apellido'] = 'Nieves'
estudiantes['sexo'] = 'Masculino'
estudiantes['edad'] = 33
estudiantes['estado civil'] = 'Soltero'
estudiantes['habilidades'] = ['Python', 'Java', 'C']
estudiantes['pais'] = 'México'
estudiantes['ciudad'] = 'Querétaro'
estudiantes['direccion'] = 'Calle sin nombre sin número'
print(len(estudiantes))
print(type(estudiantes['habilidades']))
estudiantes['habilidades'].append('C++')
estudiantes['habilidades'].append('JavaScript')
print(estudiantes.keys())
print(estudiantes.values())
print(estudiantes.items())
estudiantes.pop('direccion')
print(estudiantes)
del perro