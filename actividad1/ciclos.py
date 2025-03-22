"""
a) Itera de 0 a 10 usando cualquier ciclo.
b) Itera de 10 a 0 usando cualquier ciclo.
c) Escribe un ciclo que haga siete llamadas a print(), de modo que obtengamos en la salida
el siguiente triángulo:
 #
 ##
 ###
 ####
 #####
 ######
 #######
d) Utiliza ciclos anidados para crear lo siguiente:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
e) Imprime el siguiente patrón:
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
d) Itera a través de la lista, ['Python', 'Numpy','Pandas','Django', 'Flask'] usando un ciclo
for e imprime los elementos.
e) Utiliza el ciclo for para iterar de 0 a 100 e imprimir solo números pares.
f) Utiliza el ciclo for para iterar de 0 a 100 e imprimir solo números impares."""
size = 8
for i in range(0,11):
    print(i)
    
while i >= 0:
    print(10-i)
    i-=1

for i in range(1,size):
    print("#"*i)    

for i in range(size):
    print("# # # # # # # #")

for i in range(11):
    print(f"{i} x {i} = {i*i}")

for i in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(i)

for i in range(101):
    if i%2 == 0:
        print(i)

for i in range(101):
    if i%2 != 0:
        print(i)