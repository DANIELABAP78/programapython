num = 100
while num > 0:
    print('Ainda tem estoque')
    num = num-1
    print(num)
else:
    print('Acabou o estoque, fazer novo pedido!')
    
    balde = 0
    while balde < 10:
        print('Balde está enchendo!')
        balde = balde + 1
        print(balde)
    else:
        print('Balde está cheio!')
        
# Solicita uma entrada do usuário
entrada = input("Digite um número: ")

# Converte a entrada para um número (float neste caso)
numero = float(entrada)

# Realiza um cálculo (por exemplo, eleva o número ao quadrado)
resultado = numero ** 2

# Exibe o resultado
print(f"O quadrado de {numero} é {resultado}")
