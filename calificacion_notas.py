#hola

print ("hola")

calificaciones=["suspenso", "sufi", "bien", "notable", "sobresaliente"]
            #0          1       2       3       4

continuar=1
while continuar == 1:

    print ("Dime tu nota")
    nota = int (input ())
    if nota == 10 or nota == 9:
        print(calificaciones[4])
    elif nota== 8 or nota == 7 : 
        print(calificaciones[3])
    elif nota== 6:
        print(calificaciones[2])
    elif nota==5:
        print(calificaciones[1])
    elif nota<5 and nota >-1:
        print(calificaciones[0])
    else :
        print("vuelve a la escuela que eso no existe")

    print(" Para volver a comprobar, pulse 1, para terminar pulse otra tecla")
    del continuar

    continuar = int (input ())
    

print("Adios")
