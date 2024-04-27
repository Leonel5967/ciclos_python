numerador=1
denominador=4
sw=0
contador=0
cade=""
suma=0
while(contador<5):
    if(sw==0):
        cade=cade+str(numerador)+"/"+str(denominador)+" + "
        suma=suma+numerador/denominador
        sw=1
    else:
        cade=cade+str(numerador)+"/"+str(denominador)+" + "
        suma=suma+numerador/denominador
        sw=0
    numerador=numerador+2
    denominador=denominador*4
    contador +=1
cade=cade+" = "+str(suma)
print(cade)