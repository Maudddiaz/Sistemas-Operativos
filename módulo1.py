Contador_P = 0 #contador de programa segun el diagrama de flujo


class Proceso:#defino por asi decirlo el registro de proceso como en pseudocodigo
    def __init__(self, tamaño, tiempo):
        self.tamaño = tamaño
        self.tiempo = tiempo

class Memoriaparticion:
    def __init__(self,tamañooriginal,tamañoactual,estado):
        self.tamañooriginal = tamañooriginal
        self.tamañoactual   = tamañoactual
        self.estado = estado # estado ocupado o desacupado son 

memoria =[]
nuevo = []#no ocupa memoria
listo = []# habrian 2 aqui y el 3ero supongo que estaria en ejecucion
l_s = []# no ocupa memoria los listos suspendidos
ejecucion = []#no se cuantos procesos se pueden tener en ejecucion a la vez esto queda hablarlo
Terminado = []# no ocupa me moria

memoria.append(memoriaparticion(100,100,libre))
memoria.append(memoriaparticion(250,250,libre))
memoria.append(memoriaparticion(150,150,libre))
memoria.append(memoriaparticion(50,50,libre)) #god


nuevo.append(Proceso(50,3))# el append lo que hace es añadir un nuevo elemento en ese arreglo dinamico
nuevo.append(Proceso(100,1))

for particiones in reversed(memoria): #el reversed basicamente lo que hace es recorrer el arreglo de atras para adelante
    if particiones <> 1 
        if nuevo[1].tamaño <= memoria.tamañooriginal[particiones]:#nuevo[1].tamaño es el primer Proceso en la cola   y lo tomo para agarrar la primera referencia
            memoria.tamañoactual[particiones] = memoria.tamañoactual[particiones] - nuevo[1].tamaño
            listo.append(nuevo[1])
            break#basicamente me sale del ciclo for
    
if Contador_P <> 10 # nose como seguir :v
    
    
