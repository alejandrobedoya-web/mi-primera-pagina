# Tarea 2 - Ejercicios Unidad 1
Hola, a continuacion le damos solucion a la tarea 2 de la unidad 1
## Reto1: simula el comportamiento de la tortuga usando solo print() e input().
### solucion reto 1
```python
def tortuga_camina_adelante ():                                                 # defino una funcion
    pasos = int(input("¿cuantos pasos va dar la tortuga hacia adelante?: "))    # definimos la variable 'pasos' agregando un input para que el usuario ingrese el numero de pasos
    adelante = ("-" * pasos + ">")                                               # definimos las variable 'adelante' que va multiplicar los pasos por quines y al final agrega una '>' que es la cabeza de la tortuga en direccion hacia adelante
    print ("la tortuga da",pasos,"pasos hacia adelante")                        # imprimo la descripcion de los pasos que da la tortuga
    print(adelante)                                                             # imprimo la cariable 'adelante'
tortuga_camina_adelante ()                                
```
resultado:

<img width="685" height="226" alt="image" src="https://github.com/user-attachments/assets/87a4990f-0166-4f50-9334-ec8440b6ce42" />

## Reto 2 : Crea el rastro de una tortuga moviéndose hacia abajo usando únicamente print() e input().
### solucion reto 2
para esta solucion se realiza una recursion, recemos para que salga
```python
def tortuga_camina_abajo (pasos_abajo):                                         #defino la funcion para que la tortuga camine hacia abajo, asignandole una variable 'pasos_abajo'
  if pasos_abajo == 0:                                                          #asigno la condicion para que finalice el ciclo que en este caso es que si la cantidad de pasos llegua a 0 entonces imprimir '↓' que sera la cabeza de la tortuga
    print ("↓")
  else:                                                                          # si la anterior condicion es negativa entonces va a imprimir '|', 
    print ("|")
    tortuga_camina_abajo(pasos_abajo - 1)                                        # el valor 'pasos_abajo' en la funcion 'tortuga_camina_abajo' se le va restar 1. asi hasta que llegue a 0.

num_pasos_abajo = int(input("¿cuantos pasos va dar la tortuga hacia abajo?: "))  #creamos la variable 'num_pasos_abajo' con el fin de que el usuario indique el numero de pasos que desea
print ("la tortuga da",num_pasos_abajo,"pasos hacia abajo")                      #imprimo la descripcion de los pasos que da la tortuga
tortuga_camina_abajo(num_pasos_abajo)                                            #llamamos la funcion anteriormente creada y se asignamos la variable 'num_pasos_abajo', para que el valor que dá el usuario se guarde automaticamente en la funcion creada, y asi se inicia y cierra la recursion.
```

resultado

<img width="753" height="446" alt="image" src="https://github.com/user-attachments/assets/82625a0d-18b4-4bd1-8b22-1e2ad659d48f" />


