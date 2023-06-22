import json

# Load stock data from JSON file


def carregarDadosEstoque():
    try:
        with open('stock_data.json') as file:
            stockData = json.load(file)
    except FileNotFoundError:
        stockData = {}
    return stockData

# Save stock data to JSON file


def saveStockData(stockData):
    with open('stock_data.json', 'w') as file:
        json.dump(stockData, file)

# Create a new product in the stock


def criarProduto(stockData):
    nome = input("Digite o nome do produto: ")

    while True:
        try:
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            break
        except ValueError:
            print("Input inválido. Insira um valor válido.")

    stockData[nome] = {'preco': preco, 'quantidade': quantidade}
    saveStockData(stockData)
    print(f"Produto '{nome}' adicionado ao estoque.")

# Update an existing product in the stock


def atualizarProduto(stockData):
    nome = input("Digite o nome do produto: ")

    while True:
        try:
            if nome in stockData:
                preco = float(input("Preço do produto atualizado: "))
                quantidade = int(input("Quantidade do produto atualizado: "))

                stockData[nome]['preco'] = preco
                stockData[nome]['quantidade'] = quantidade
                saveStockData(stockData)
                print(f"Produto '{nome}' atualizado no estoque.")
            else:
                print(f"Produto '{nome}' não encontrado.")
        except ValueError:
            print("Input inválido. Insira um valor válido.")


# Delete a product from the stock


def deletarProduto(stockData):
    nome = input("Digite o nome do produto: ")
    if nome in stockData:
        del stockData[nome]
        saveStockData(stockData)
        print(f"Produto '{nome}' deletado do estoque.")
    else:
        print(f"Produto '{nome}' não encontrado.")

# Display the current stock data


def mostrarEstoque(stockData):
    print("Estoque atual:")
    for nome, produto in stockData.items():
        print(
            f"Nome: {nome}, Preco: {produto['preco']}, Quantidade: {produto['quantidade']}")

# Main program loop


# Sell a product from the stock
def venderProduto(stockData):
    nome = input("Digite o nome do produto a ser vendido: ")
    if nome in stockData:
        quantidadeParaVender = int(input("Digite a quantidade a ser vendido: "))
        quantidadeAtual = stockData[nome]['quantidade']

        if quantidadeParaVender <= quantidadeAtual:
            stockData[nome]['quantidade'] -= quantidadeParaVender
            saveStockData(stockData)
            print(f"Foram vendido {quantidadeParaVender} {nome}(s).")
        else:
            print(f"Não tem quantidade suficiente para {nome}.")
    else:
        print(f"Produto '{nome}' não encontrado.")

# Main program loop


def main():
    stockData = carregarDadosEstoque()

    while True:
        print("\nSistema de estoque: ")
        print("1. Criar um produto")
        print("2. Atualizar um produto")
        print("3. Deletar um produto")
        print("4. Mostrar estoque")
        print("5. Vender um produto")
        print("6. Exit")

        escolha = input("Escolha alguma ação (1-6): ")

        if escolha == '1':
            criarProduto(stockData)
        elif escolha == '2':
            atualizarProduto(stockData)
        elif escolha == '3':
            deletarProduto(stockData)
        elif escolha == '4':
            mostrarEstoque(stockData)
        elif escolha == '5':
            venderProduto(stockData)
        elif escolha == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()
