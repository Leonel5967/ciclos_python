#c)	2/3, -4/9, 8/27, -16/81, 32/243...N
numerador=2
denominador=3
contador=1
sw=0
while(contador<=5):
    if(sw==0):
        print(numerador ,"/",(denominador))
        sw=1
    else:
        print(-numerador ,"/",(denominador))
        sw=0
    numerador=numerador*2
    denominador=denominador*3
    contador=contador+1