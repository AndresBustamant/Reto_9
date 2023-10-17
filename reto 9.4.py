import math
def area_esfera(*args) -> float:
    areaesfe= 4* math.pi* r1**2
    return areaesfe
def area_cono(*args) -> float:
    areacon= math.pi*r2(r2+ (r2**2+h**2)**1/2)
    return areacon
def volumen_esfera(*args) -> float:
    volumenesfe= (4* math.pi*r1**3)/3
    return volumenesfe
def volumen_cono(*args) -> float:
    volumencon= (math.pi*r2**2*h)/33
    return volumencon

def volumen_total(*args) -> float:
    return (math.pi*r2**2*h)/3 + (4* math.pi*r1**3)/3
def area_total(*args) :
    return (4* math.pi* (r1**2)) + (math.pi*r2*(math.sqrt(r2+ (r2**2+h**2))))

if __name__ == "__main__":
    r1= int(input("ingresa el radio de la esfera:"))
    r2= int(input("ingresa el radio del cono:"))
    h= int(input("ingresa la altura del cono:"))
    volumen= volumen_total(r1,r2,h)

    area= area_total(r1,r2,h)
    print("el voluen superficial de la figura es " +str(volumen))
    print("el area superficial de la figura es " +str(area))