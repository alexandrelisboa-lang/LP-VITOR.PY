import os 
os.system("cls")
vetor_nota= []
QUANTIDADE_NUMERO=5


for i in range (QUANTIDADE_NUMERO):
    numero=int(input(f"digite o  {i+1}ª numero: "))
    vetor_nota.append(numero)
    maior = max (vetor_nota)
    menor = min (vetor_nota) 
               
print ("\n---- resultado-----")
print (f"numeros informados:{numero}")
print(f" o maior numero e : {maior}")
print(f"menor numero e: {menor}")        