
notas = {
    10: "Sobresaliente Alto",
    9:  "Sobresaliente Bajo",
    8:  "Notable Alto",
    7:  "Notable Bajo",
    6:  "Bien",
    5:  "Sufi",
    4:  "Suspenso, pringao",
    3:  "Suspenso, pringao",
    2:  "Suspenso, pringao",
    1:  "Suspenso, pringao"  
}

class Evaluacion:
    def __init__(self, notas):
        self.notas = notas
    
    def evaluame(self):
        print ("hola")
 
        continuar=1
        while continuar == 1:
            print ("Dime tu nota")
            try:
                nota_entrada = int(input ())
                self.buscar_nota(nota_entrada)
                print("Para volver a comprobar, pulse 1, para terminar pulse otra tecla")
                continuar = int(input ())
            except ValueError:
                print("vuelve a la escuela que eso no existe")
                break
        print("Adios")
    
    def buscar_nota(self, nota_entrada):
        print(f'Tu nota: {nota_entrada}')
        for key, evaluacion in self.notas.items():
            if nota_entrada == key:
                print(evaluacion)
                break
        else:
            print("La nota debe de estar entre 1 y 10")

             
init = Evaluacion(notas)
init.evaluame()

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
