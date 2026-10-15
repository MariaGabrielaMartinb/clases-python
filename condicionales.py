Edad = int(input("Que edad tienes ?")) # edad en numero entero
if Edad <0:
    # Esto solo pasa si la edad es menor a 5
    print("¡Gratis! (0€)")
elif Edad <= 5 and Edad <=17:
    # Esto pasa si lo primero falló, y la edad está entre 5 a 17 años
    print("Descuento de estudiante (5€)")
elif Edad >= 18 and Edad <=64:
    # Esto pasa si lo primero fallo, y la edad esta entre 18 a 64 años
    print("Entrada general (€17)")
else: # Esto es el "comodín": se ejecuta si ninguna de las condiciones de arriba se cumplió
    print("Descuento de adulto mayor (€-4)")