# Matheus Villar n° 21 
# Miguel Borges n° 22 
# Pedro Zocatelli n° 27 

def cadastra_produto(nome, preco, quantidade):
    return {"nome": nome, "preco": preco, "quantidade": quantidade}

produtos = []

for i in range(5):
    nome = input(f"Produto {i + 1} - Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    produtos.append(cadastra_produto(nome, preco, quantidade))

print("\nProdutos cadastrados:")
for produto in produtos:
    print(produto)
