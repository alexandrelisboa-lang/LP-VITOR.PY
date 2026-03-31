import os
os.system("cls")

vetor=[]
numeros = 5

for i in range (numeros):
    numeros= int(input(f"digite o {i+1}º numero: "))
    if numeros <0:
        numeros = 0
    
    vetor.append (numeros)
    
print("\n --- valores do vetor ---")
print (vetor)    
    