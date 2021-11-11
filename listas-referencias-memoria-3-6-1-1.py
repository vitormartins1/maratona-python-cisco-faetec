#As listas (e muitas outras entidades complexas de Python) são armazenadas 
# de formas diferentes das variáveis ordinárias (escalares).
#Pode-se dizer que:
#o nome de uma variável ordinária é o nome do seu conteúdo;
#o nome de uma lista é o nome de um local de memória onde a lista é armazenada.


list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)


#A atribuição: list_2 = list_1 copia o nome do array, não o seu conteúdo. 
# Com efeito, os dois nomes (list_1 e list_2) identificam o mesmo local na memória do computador.
# Modificar um deles afeta o outro, e vice-versa.