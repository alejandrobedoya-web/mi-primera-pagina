# Tarea 2 - Ejercicios Unidad 1
Hola, a continuacion le damos solucion a la tarea 2 de la unidad 1
## Reto1: simula el comportamiento de la tortuga usando solo print() e input().
Intenta recrear el movimiento de la tortuga únicamente con texto, usando funciones, print() y input() para pedir valores al usuario.
### solcuion reto 1
''''python
def tortuga_camina_adelante ():
    pasos = int(input("¿cuantos pasos va dar la tortuga hacia adelante?: "))
    adelante = ("-" * pasos + "B")
    print ("la tortuga da",pasos,"pasos hacia adelante")
    print(adelante)
tortuga_camina_adelante ()

