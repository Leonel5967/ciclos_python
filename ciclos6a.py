numerador=1
denominador=2
sw=0
contador=1
while(contador<=6):
    if(sw==0):
        print(numerador ,"/", (denominador))
        sw=1
    else:
        print(-numerador,"/",(denominador))
        sw=0
    denominador=denominador+1
    contador=contador+1