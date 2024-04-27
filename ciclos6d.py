#d)	-1/5, 2/10, -3/15, 4/20, -5/25...N
numerador=1
denominador=5
contador=1
sw=0
while(contador<=5):
    if(sw==0):
        print(-numerador, "/", (denominador))
        sw=1
    else:
        print(numerador, "/", (denominador))
        sw=0
    numerador=numerador+1
    denominador=denominador+5
    contador=contador+1
    
