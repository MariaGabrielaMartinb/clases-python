import random #es para que nos arroje un numero aleatorio

import time # es para que nos ponga tiempo en segundos

def temporizador(segundos): # definimos la funcion temporizador con un parametro de segundos
    print(f"Tienes {segundos} segundos para descubrirlo, ¡Comienza el temporizador!")
   

def juego_adivinanza(): # hay que colocar : para que separe la funcion del resto del codigo
    numero_secreto = random.randint (1,100) # genera un numero aleatorio entre 1 y 100
    intentos = 0 # contador de intentos
    adivinado = False # bandera para indicar si se ha adivinado el número
    print("¡Bienvenido al juego de adivinanza!")
    print("Introduce un numero entre 1 y 100 y yo tratare de avidinarlo!")

    while not adivinado:
        prueba = int(input("Introduce un numero: "))
        intentos +=1

        if prueba < numero_secreto:
            print (" Ingresa un numero mayor")
        elif prueba > numero_secreto: 
            print ("Ingresa un numero menor")
        else:
            adivinado = True
            print (f"Felicidades, adivinaste el numero secreto en {intentos} intentos!")

           

juego_adivinanza()






