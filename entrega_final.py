print("Hola, bienvenido")


def snbeca(beca):
    if beca == "si":
        print("FELICIDADES, OJALA LA MANTENGAS")
    else:
        print("Consiguete una porque la escuela esta cara:(")
beca = str(input("¿Tienes beca si o no?"))
snbeca(beca)


def prom(materia):
    if materia < 80:
        print("¡Échale más ganas!")
    else:
        print("¡Sigue así!")
materia_1 = int(input("¿Cuánto sacaste en la materia 1 del 1 al 100?"))
while materia_1 < 0 or materia_1 > 101:
    materia_1 = int(input("¿Cuánto sacaste en la materia 1 del 1 al 100?"))
prom(materia_1)

materia_2 = int(input("¿Cuánto sacaste en la materia 2 del 1 al 100?"))
while materia_2 < 0 or materia_2 > 101:
    materia_2 = int(input("¿Cuánto sacaste en la materia 2 del 1 al 100??"))
prom(materia_2)
materia_3 = int(input("¿Cuánto sacaste en la materia 3 del 1 al 100?"))
while materia_3 < 0 or materia_3 > 101:
    materia_3 = int(input("¿Cuánto sacaste en la materia 3 del 1 al 100??"))
prom(materia_3)
materia_4 = int(input("¿Cuánto sacaste en la materia 4 del 1 al 100?"))
while materia_4 < 0 or materia_4 > 101:
    materia_4 = int(input("¿Cuánto sacaste en la materia 4 del 1 al 100??"))
prom(materia_4)
materia_5 = int(input("¿Cuánto sacaste en la materia 5 del 1 al 100?"))
while materia_5 < 0 or materia_5 > 101:
    materia_5 = int(input("¿Cuánto sacaste en la materia 5 del 1 al 100??"))
prom(materia_5)
materia_6 = int(input("¿Cuánto sacaste en la materia 6 del 1 al 100?"))
while materia_6 < 0 or materia_6 > 101:
    materia_6 = int(input("¿Cuánto sacaste en la materia 6 del 1 al 100?"))
prom(materia_6)
lista = [materia_1, materia_2, materia_3, materia_4, materia_5, materia_6]


def promedio(lista):
    acum = 0.0
    for elem in lista:
        acum = acum + elem
    return acum/len(lista)

if beca == "si":
    promedio_beca = int(input("¿Cuánto promedio necesitas para mantenerla?"))
    if (promedio(lista) > promedio_beca):
        print("tu promedio final fue ", promedio(lista), " conservas la beca!")
    elif (promedio_beca == promedio):
        print("tu promedio fue", promedio(lista), " conservas la beca!")
    else:
        print("tu promedio fue", promedio(lista), "no conservas la beca:( !")
else:
    print("Tu promedio final fue de", promedio(lista))
