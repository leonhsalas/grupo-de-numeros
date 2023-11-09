elemento = int(input("Cual es el numero que vas a a agregar a la lista "))
lista = []
lista.append(elemento)
elemento = int(input("Cual es el numero que vas a a agregar a la lista "))
lista.append(elemento)
elemento = int(input("Cual es el numero que vas a a agregar a la lista "))
lista.append(elemento)
elemento = int(input("Cual es el numero que vas a a agregar a la lista "))
lista.append(elemento)
elemento = int(input("Cual es el numero que vas a a agregar a la lista "))
lista.append(elemento)



primernumero = lista[0]
contador = 1
numeroaanalizar = lista[contador]
while contador < 5:
    menos = primernumero - numeroaanalizar
    if menos < 0:
        contador2 = 1
        while menos < 0:
            menos = menos + 1
            contador2 = contador2 + 1
        if contador == 1:
            Aux1 = contador2
        elif contador == 2:
            Aux2 = contador2
        elif contador == 3:
            Aux3 = contador2
        elif contador == 4:
            Aux4 = contador2
        contador2 = 0
    if menos > 0:
        contador3 = 1
        while menos > 0:
            menos = menos - 1
            contador3 = contador3 + 1
        if contador == 1:
            Aux1 = contador3
        elif contador == 2:
            Aux2 = contador3
        elif contador == 3:
            Aux3 = contador3
        elif contador == 4:
            Aux4 = contador3
        contador3 = 0
    menos = primernumero - numeroaanalizar
    if menos == 0:
        resultado = numeroaanalizar
        break
    contador = contador + 1
    if contador == 5:
        pass
    else:
        numeroaanalizar = lista[contador]

if Aux1 < Aux2 and Aux1 < Aux3 and Aux1 < Aux4:
    resultado = lista[1]
elif Aux2 < Aux1 and Aux2 < Aux3 and Aux2 < Aux4:
    resultado = lista[2]
elif Aux3 < Aux2 and Aux3 < Aux1 and Aux3 < Aux4:
    resultado = lista[3]
elif Aux4 < Aux2 and Aux4 < Aux3 and Aux4 < Aux1:
    resultado = lista[4]

print(resultado)