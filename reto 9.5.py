import math
def area_base_circular(*args) -> float:
    area_circular= math.pi*r**2
    return area_circular
def area_cuadrada(*args) -> float:
    area_cuadrado= 2*math.pi* a*b
    return area_cuadrado
def area_total(*args) -> float:
    areat= 2*math.pi*a*b + 2*math.pi*r**2
    return areat
def perimetro_base_circular(*args) -> float:
    perimetro_circular= 2*math.pi*r
    return perimetro_circular
def perimetro_cuadrada(*args) -> float:
    perimetro_cuadrado= a*b
    return perimetro_cuadrado
def perimetro_total(*args) -> float:
    perimetrot= 2*math.pi*r + a*b
    return perimetrot
if __name__ == "__main__":
    r= int(input("ingresa el radio de la base:"))
    b= int(input("ingresa lo que mide la base cuadrada:"))
    a= int(input("ingresa la altura de la parte cuadrada:"))
    area= area_total(r,a,b)
    perimetro= perimetro_total(r,a,b)
    print("el perimetro superficial de la figura es " +str(perimetro))
    print("el area superficial de la figura es " +str(area))