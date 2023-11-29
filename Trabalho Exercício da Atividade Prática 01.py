# Print de boas-vindas
print('Bem-vindo à loja do Douglas Wesley Alves de Oliveira')

# Valor unitário e quantidade
valor_produto = float(input('Entre com o valor desejado: '))
qtd_produto = int(input('Entre com a quantidade do produto: '))
desconto_produto = 0

# Estrutura if, elif, else para calcular o desconto
if qtd_produto <= 200:
    desconto_produto = 0.00
elif 200 < qtd_produto <= 1000:
    desconto_produto = 0.05
elif 1000 < qtd_produto <= 2000:
    desconto_produto = 0.10
else:
    desconto_produto = 0.15

# Resultado
total_sem_desconto = valor_produto * qtd_produto
print('O valor total SEM desconto é de: R$ {:.2f}'.format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print('O valor total COM desconto é de: R$ {:.2f}'.format(total_com_desconto))
