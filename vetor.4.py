import os 
os.system("cls")

vetor_notas=[]

QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    nota= float(input(f"digite a {i+1}ª notas: "))
    vetor_notas.append(nota)
    media = sum(vetor_notas) / QUANTIDADE_NOTAS
    
    
if media >= 7:
        print(f"APROVADO,media {media}")
elif media >= 5 and media <6.9:
        print(f"RECUPERAÇAO, media {media} ")
else:
         print(f"REPROVADO,media{media}")       
         
for i, uma_nota  in enumerate(vetor_notas, start = 1):
 print ( f"{i}ª nota {uma_nota}")