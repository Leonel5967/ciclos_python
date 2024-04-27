numerador=3
denominador=4
contador=1
sw=0
while(contador<=6):
    if(sw==0):
        print(-numerador, "/", (denominador))
        sw=1
    else:
        print(numerador, "/", (denominador))
        sw=0
    numerador=numerador+2
    denominador=denominador*2
    contador=contador+1