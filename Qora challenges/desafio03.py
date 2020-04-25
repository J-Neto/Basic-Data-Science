# DESAFIO REPETIÇÃO
# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.
# qual numero voce deseja receber a sequencia fibonacci? 34

#José Ribeiro Neto

num = int(input('Qual número você deseja receber a sequência fibonacci?'))
ant = 0
atual = 1
inter = 0

while(atual <= num):
    print(atual)
    inter = atual
    atual = atual + ant
    ant = inter