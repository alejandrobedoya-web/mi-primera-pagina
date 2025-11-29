# Tarea 2 - Ejercicios Unidad 1
Hola, a continuacion le damos solucion a la tarea 2 de la unidad 1
## Reto1: simula el comportamiento de la tortuga usando solo print() e input().
### solucion reto 1
```python
pasos = int(input("¿cuantos pasos va dar la tortuga hacia adelante?: "))
adelante = ("-" * pasos + ">")
print ("la tortuga da",pasos,"pasos hacia adelante")
print(adelante)                        
```
resultado:

<img width="632" height="262" alt="image" src="https://github.com/user-attachments/assets/400b724c-f206-4eba-9954-4ba0b2e2f84d" />


## Reto 2 : Crea el rastro de una tortuga moviéndose hacia abajo usando únicamente print() e input().
### solucion reto 2
para esta solucion se realiza una recursion, recemos para que salga
```python
def tortuga_camina_abajo (pasos_abajo):                                         #defino la funcion para que la tortuga camine hacia abajo, asignandole una variable 'pasos_abajo'
  if pasos_abajo == 0:                                                          #asigno la condicion para que finalice la recursion, que en este caso es que si la cantidad de pasos llegua a 0 entonces imprimir '↓' que sera la cabeza de la tortuga
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

## Reto 4: Encapsula los comportamientos anteriores usando funciones
Reescribe los retos anteriores creando funciones que representen los movimientos de la tortuga solo con texto.
### solucion reto 2
Para esta solucion, reescribí los retos anteriores para que cumplieran con los parametros del reto 4
```python
## solucion reto 1 y 2 modificado para que cumpla con reto 4
def adelante (n):                          #defino la funcion adelante   
    pasos = ("-" * n + ">"                 #creo la variable 'pasos' que va multiplicar el valor de 'n' por los guiones y al final agrega una '>' que es la cabeza de la tortuga en direccion hacia adelante
    print(pasos)                           #imprimo los el resultado
   
def abajo (n, m):                          #defino la funcion abajo, va tener dos variable: 'n' para los pasos abajo y 'm' para los espacios a la derecha que debe ser igual a los pasos hacia adelante que se ponen en la funcion 'adelante'
  espacios = " " * m                       #defino la variable 'espacios' que multiplica un espacion en blanco por 'm'           
  if n == 0:                               #asigno la condicion para que finalice la recursion que en este caso es que si la cantidad de pasos llegua a 0 entonces imprimir espacios + '↓' que sera la cabeza de la tortuga
    print (espacios + "↓")               
  else:
    print (espacios + "|")                  # si la anterior condicion es negativa entonces va a imprimir espacios + '|'          
    abajo(n - 1, m) 

adelante (5)                                # asignamos el valor en la funcion adelante
abajo (3, 5)                                # asignamos los valoes de abajo, la primera funcion es los pasos abajo y la segunda es la cantidad de espacios a la derecha(debe ser igual a el valor de adelante)
```
Esto fue lo más cerca que estuve para darle una solucion al reto 4, no encontraba la forma de asignarle el movimiento hacia abajo con los espacios que deja el moviemiento adelante de forma automatica.

Resultado

<img width="718" height="444" alt="image" src="https://github.com/user-attachments/assets/d70029cf-62f1-4183-baa9-a5244854dd5d" />


