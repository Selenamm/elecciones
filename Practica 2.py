def obtenerPrecio(cantllanta):
    total=0
    if (cantllanta >=5):
        total= (cantllanta*70000)
    else:
         total= (cantllanta*80000)
    print("El precio es: ",total)

def calcularPrecio():
    precio=int(input("Ingrese la cantidad de llantas:"))
    resultado=obtenerPrecio(precio)
    return("El precio es: "+ str(resultado))
calcularPrecio()


