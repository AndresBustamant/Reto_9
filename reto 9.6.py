panes = 300
leche = 3300
huevos = 350
B:int
def precio_a_pagar (*args) ->int:
    precio_panes= p*panes
    precio_leche= m*leche
    precio_huevos= h*huevos
    precio_total= (p*panes)+(m*leche)+(h*huevos)
    devuelta= B - precio_total
    if devuelta<0:
        print("hace falta dinero para pagar")
    else:
      return devuelta

if __name__ == "__main__":
    p= int(input("ingresa la cantidad de panes:"))
    m= int(input("ingresa la cantidad de bolsas de leche:"))
    h= int(input("ingresa la cantidad de huevos:"))
    B= int(input("ingresa la cantidad de dinero que te dieron: "))
    devueltas= precio_a_pagar(p,m,h)
    print("la cantidade de dinero restante es " +str(devueltas))