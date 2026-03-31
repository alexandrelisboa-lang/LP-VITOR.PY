import os 
os.system("cls")

soma= 0
vetor=[]
NU = 5
negativo = 0


for i in range(NU):
        numero=int(input(f"digite o {i+1}º numero:  "))
        vetor.append(numero)
        
for numero in vetor:
    if numero < 0:
        negativo +=1
    elif numero > 0:
        soma += numero
        
print(f"a quantidade de numeros negativo e {negativo} \ne a soma dos numeros positivos e {soma}")