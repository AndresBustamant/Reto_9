n: int
i: int
def potencia(n:int, i:int)->int:
  if i==0:
    return 1
  elif i==1:
    return n
  else:
    return n**i

if __name__ == "__main__":
  n = int(input("Ingrese numero base de la potencia: "))
  i = int(input("ingresa el expinente de la potencia: "))
  resultpotencia = potencia(n,i)
  print("el resultado de la potencia con base " + str(n) + " elevadas a " +str(i)+ " es " + str(resultpotencia))