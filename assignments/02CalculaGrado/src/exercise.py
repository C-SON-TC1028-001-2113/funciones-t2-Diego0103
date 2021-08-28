def calcula_grado(numero):
    if numero>0.9 and numero<=1.0:
        return "A"
    elif numero>0.8 and numero<=1.0:
        return "B"
    elif numero>0.7 and numero<=1.0:
        return "C"
    elif numero>0.6 and numero<=1.0:
        return "D"
    elif numero>=0 and numero<=1.0:
        return "F"
    else:
        return "score incorrecto"
def main():
    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))

if __name__=='__main__':
    main()
