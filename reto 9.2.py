Gallina = 6
Gallo = 7
pollo = 1

if __name__ == "__main__":
    n= int(input("ingresa la cantidad de gallinas:"))
    m= int(input("ingresa la cantidad de gallos:"))
    k= int(input("ingresa la cantidad de pollos:"))
    carneT= lambda n,m,k: n*Gallina + m*Gallo + k*pollo
    carne = carneT(n,m,k)
    print("la cantidade de carne en total es " +str(carne)+ "Kg")