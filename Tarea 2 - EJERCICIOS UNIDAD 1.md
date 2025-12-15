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
### Solución reto 4

Para esta solucion, reescribí los retos anteriores para que cumplieran con los parametros del reto 4
```python
## solucion reto 1 y 2 modificado para que cumpla con reto 4
espacios = 0   
def adelante (n):
    global espacios                                               # llamo esa variable con global para que su valor se modifique y se pueda capturar en las funciones constantemente
    print(espacios * " " + "-" * n + ">" )
    espacios = espacios + n
def abajo (n):
  if n == 0:
    print (" " * espacios + "↓")
  else:
    print (" " * espacios + "|")
    abajo(n - 1)
```
Resultado
<img width="587" height="467" alt="image" src="https://github.com/user-attachments/assets/0e5698d1-dc08-4161-bace-07795db7238e" />

## Reto 5: La tortuga baja las escalas
### solucion reto 5
Se usa las mismas lines de codigo anterior ya que el contador de espacios permite hacer que la tortuga recurde su posicion 

```python
espacios = 0   
def adelante (n):
    global espacios                               
    print(espacios * " " + "-" * n + ">" )
    espacios = espacios + n
def abajo (n):
  if n == 0:
    print (" " * espacios + "↓")
  else:
    print (" " * espacios + "|")
    abajo(n - 1)
```
 resultado 

 <img width="469" height="653" alt="image" src="https://github.com/user-attachments/assets/a9a80598-aaee-4b31-be31-6bbf9eaa4ed5" />


## Enlace de la actividad realizada 
https://colab.research.google.com/drive/1kxjbRVtjQJ56e_iuCP-DYAoMauAWhV4M?usp=sharing

## Uso de IA 
Se usa Gemini como asistente dentro de Colab, el cual no me comparte el link con el historial de conversacion
