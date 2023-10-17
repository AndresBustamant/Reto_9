if __name__ == "__main__":
    p= int(input("ingresa la poblacion inicial:"))
    d= int(input("ingresa los dias transcurridos:"))
    contagt= lambda p,d: p*(2**d)
    contag= contagt (p,d)
    print("la poblacion contagiada es de " +str(contag))