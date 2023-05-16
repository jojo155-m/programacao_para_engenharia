numeros []
#teste

while True:
    num = int(input("digitar um valor positivo -1 para parar "))

    if num ==-1:
        break

    if num > 0:
        numeros.append (num)

if len (numeros) == 0 :
    print ("nenhum número positivo foi digitado")

else:
    soma = num(numeros)
    media= soma /len (numeros)
    menor = min(numeros)
    maior = max (numeros )  

    print("soma dos numeros :", soma)
    print("medía dos numeros :",media)
    print("menos numeros ", menor)
    print("maior numeros ", maior )      
