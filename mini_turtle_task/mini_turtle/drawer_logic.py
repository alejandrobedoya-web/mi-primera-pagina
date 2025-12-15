import mi_turtle

espacios = 0       

def adelante (n):
   global espacios                                             
   print(espacios * " " + "-" * n + ">" )
   espacios = espacios + n

def abajo (n):
  for a in range (n):
    print(" " * espacios +"|")
  print (" " * espacios +"↓")

## funcion adicional reiniciar

def reiniciar ():
  global espacios
  espacios = 0
  print ("se reinició la posicion de la tortuga")

