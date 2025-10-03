Contador_P = 0 #contador de programa segun el diagrama de flujo
memoria = [100,250,150,50]#la memoria fija que cada vez que este algo ahi se le resta el tamaño del proceso

class Proceso:#defino por asi decirlo el registro de proceso
    def __init__(self, tamaño, tiempo):
        self.tamaño = tamaño
        self.tiempo = tiempo 

nuevo = []
listo = []
l_s = []
ejecucion = []#no se cuantos procesos se pueden tener en ejecucion a la vez esto queda hablarlo
Terminado = []

nuevo.append(Proceso(50,3))# el append lo que hace es añadir un nuevo elemento en ese arreglo dinamico
nuevo.append(Proceso(100,1))

for particiones in reversed(memoria): #el reversed basicamente lo que hace es recorrer el arreglo de atras para adelante
    if particiones <> 1 
        if nuevo[1].tamaño <= memoria[particiones]:#nuevo[1].tamaño es el primer Proceso en la cola   y lo tomo para agarrar la primera referencia
            memoria[particiones]:= memroia[particiones] - nuevo[1].tamaño
            listo.append(nuevo[1])
            break#basicamente me sale del ciclo for
    
if Contador_P <> 10
    
    
