#f)	-1/3, 2/9, -3/27, 4/81, -5/243...N
numerador=1
denominador=3
contador=1
sw=0
while(contador<=5):
    if(sw==0):
        print(-numerador,"/",(denominador))
        sw=1
    else:
        print(numerador,"/",(denominador))
        sw=0
    numerador=numerador+1
    denominador=denominador*3
    contador=contador+1