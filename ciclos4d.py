numero=5
contador=1
incre=5
sw=0
while(contador<=6):
    if(sw==0):
        print(numero)
        sw=1
    else:
        print(-numero)
        sw=0
    numero=numero+incre
    contador=contador+1