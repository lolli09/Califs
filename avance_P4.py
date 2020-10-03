print("Hola, bienvenido")

beca=str(input("¿Tienes beca?"))
def beca_sn(beca):
    return (beca)

materia_1=int(input("¿Cuánto sacaste en la materia 1 (en centécimas)?"))
def por_tareas(materia_1):
    while materia_1>0:
        if materia_1 < 80:
            print("¡Échale más ganas!")
        else:
            print("¡Sigue así!")


materia_2=int(input("¿Cuánto sacaste en la materia 2  (en centécimas)?"))
def por_examen(materia_2):
    while materia_1>0:
        if materia_1<80:
            print("¡Échale más ganas!")
        else:
            print("¡Sigue así!")

materia_3=int(input("¿Cuánto sacaste en la materia 3 (en centécimas)?"))
def por_actividades(materia_3):
    while materia_1>0:
        if materia_1<80:
            print("¡Échale más ganas!")
        else:
            print("¡Sigue así!")
        
materia_4=int(input("¿Cuánto sacaste en la materia 4  (en centécimas)?"))
def por_proyecto(materia_4):
    return (materia_4)
    if materia_1<80:
        print("¡Échale más ganas!")
    else:
        print("¡Sigue así!")
              
materia_5=int(input("¿Cuánto sacaste en la materia 5  (en centécimas)?"))
def por_proyecto(materia_5):
    while materia_1<0:
        if materia_180:
            print("¡Échale más ganas!")
        else:
            print("¡Sigue así!")

materia_6=int(input("¿Cuánto sacaste en la materia 6  (en centécimas)?"))
def por_proyecto(materia_6):
    while materia_1>0:
        if materia_1<80:
            print("¡Échale más ganas!")
        else:
            print("¡Sigue así!")

lista=[materia_1, materia_2, materia_3, materia_4, materia_5, materia_6]

def promedio(lista):
    acum = 0.0
    for elem in lista:
        acum = acum + elem
    return acum/len(lista)

if beca == "si":
        promedio_beca=int(input("¿Cuánto promedio necesitas para mantenerla?"))
        if (promedio(lista) > promedio_beca):
            print("¡Felicidades, tu promedio final fue de ", promedio(lista), "y afortunadamente conservas la beca!")
        elif (promedio_beca==promedio):
            print("¡Esfuerzate más, tu promedio fue de ", promedio(lista), "y por poco no conservas la beca!")
        else:
            print("¡Lo siento, tu promedio fue de ", promedio(lista), "y lamentablemente no conservas la beca!")  
else:
    print("Tu promedio final fue de", promedio)

                
            
