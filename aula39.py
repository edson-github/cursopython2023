"""
Iterando strings com while
"""

#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nome = 'Maria Helena'  # Iteráveis

novo_nome = ''
for indice in range(len(nome)):
    letra = nome[indice]
    novo_nome += f'*{letra}'
novo_nome += '*'
print(novo_nome)
