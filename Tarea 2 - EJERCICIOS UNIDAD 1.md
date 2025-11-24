# Tarea 2 - Ejercicios Unidad 1
Hola, a continuacion le damos solucion a la tarea 2 de la unidad 1
## Reto1: simula el comportamiento de la tortuga usando solo print() e input().
### solucion reto 1
```python
def tortuga_camina_adelante ():
    pasos = int(input("¿cuantos pasos va dar la tortuga hacia adelante?: "))
    adelante = ("-" * pasos + "B")
    print ("la tortuga da",pasos,"pasos hacia adelante")
    print(adelante)
tortuga_camina_adelante ()
```
resultado:

<img width="685" height="226" alt="image" src="https://github.com/user-attachments/assets/87a4990f-0166-4f50-9334-ec8440b6ce42" />

## Reto 2 : Crea el rastro de una tortuga moviéndose hacia abajo usando únicamente print() e input().
### solucion reto 2
para esta solucion se realiza una recursion, recemos para que salga
```python
pasos_abajo = int(input("¿cuantos pasos va dar la tortuga hacia abajo?: "))
print ("la tortuga da",pasos_abajo,"pasos hacia abajo")

def tortuga_camina_abajo (pasos_abajo):
  if pasos_abajo == 0:
    print ("↓")
  else:
    print ("|")
    tortuga_camina_abajo(pasos_abajo - 1)
tortuga_camina_abajo(pasos_abajo)
```

resultado

<img width="718" height="359" alt="image" src="https://github.com/user-attachments/assets/1493d0a0-0be3-49e5-b945-58450f7257fd" />

