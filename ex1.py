"""
Crie uma lista vazia;
Adicione os elementos: 1, 2, 3, 4 e 5,  usando append();
Imprima a lista;
Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);
Imprima a lista modificada;
Imprima também o tamanho da lista usando a função len();
Altere o valor do último elemento para 6 e imprima a lista modificada."""

lista = []

for _ in range(1, 6):
    lista.append(_)
    
print('elementos na lista', lista)

lista.remove(3)
print('elementos na lista', lista)