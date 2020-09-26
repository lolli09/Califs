
"""#ciclo basico
i = 10  #contador
while i > 0:   #condicion
    print("i vale :", i)
    i = i - 1 # incremento
print("")"""

beca=str(input("¿Tienes beca?"))
def beca_sn(beca):
    return (beca)

materia_1=int(input("¿Cuánto sacaste en la materia 1 (en centécimas)?"))
def por_tareas(materia_1):
    while materia_1<0:
        print("Error, debería ser positivo")
        numero = int(input("Ingresa de nuevo")
        if materia_1<80:
        print("¡Échale más ganas!")
    else:
        print("¡Sigue así!")


materia_2=int(input("¿Cuánto sacaste en la materia 2  (en centécimas)?"))
def por_examen(materia_2):
    while materia_1<0:
        print("Error, debería ser positivo")
        numero = int(input("Ingresa de nuevo")
    if materia_1<80:
        print("¡Échale más ganas!")
    else:
        print("¡Sigue así!")

materia_3=int(input("¿Cuánto sacaste en la materia 3 (en centécimas)?"))
def por_actividades(materia_3):
    while materia_1<0:
        print("Error, debería ser positivo")
        numero = int(input("Ingresa de nuevo")
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
        print("Error, debería ser positivo")
        numero = int(input("Ingresa de nuevo")
    if materia_1<80:
        print("¡Échale más ganas!")
    else:
        print("¡Sigue así!")

materia_6=int(input("¿Cuánto sacaste en la materia 6  (en centécimas)?"))
def por_proyecto(materia_6):
    while materia_1<0:
        print("Error, debería ser positivo")
        numero = int(input("Ingresa de nuevo")
    if materia_1<80:
        print("¡Échale más ganas!")
    else:
        print("¡Sigue así!")
        
promedio=((materia_1+materia_2+materia_3+materia_4+materia_5+materia_6)/6)
def promedio_materias(promedio):
    return(promedio)

if beca == "si":
    promedio_beca=int(input("¿Cuánto promedio necesitas para mantenerla?"))
    def mantener_beca(promedio_beca, promedio):
        if (promedio_beca>promedio):
            print("¡Felicidades, tu promedio final fue de ", promedio, "y afortunadamente conservas la beca!")
        elif (promedio_beca==promedio):
            print("¡Esfuerzate más, tu promedio fue de ", promedio, "y por poco no conservas la beca!")
        else:
            print("¡Lo siento, tu promedio fue de ", promedio, "y lamentablemente no conservas la beca!")  
else:
    print("Tu promedio final fue de", promedio)

                
            
