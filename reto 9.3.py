if __name__ == "__main__":
    ci= int(input("ingresa el capital prestado:"))
    i= int(input("ingresa el interes anual:"))
    n= int(input("ingresa los años a los que quieres proyectr el interes:"))
    intercompuest= lambda ci,i,n: ci*(1+ i)**n
    capital= intercompuest(ci,i,n)
    print("el capital final es de " +str(capital))