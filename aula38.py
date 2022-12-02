"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

qtd_linhas = 5
qtd_colunas = 5

for linha in range(1, qtd_linhas + 1):
    for coluna in range(1, qtd_colunas + 1):
        print(f'{linha=} {coluna=}')
print('Acabou')
