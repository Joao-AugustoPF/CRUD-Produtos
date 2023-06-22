# Sistema de Estoque

Este é um projeto de um sistema simples de estoque em Python, que permite criar, atualizar, excluir e vender produtos. Os dados do estoque são armazenados em um arquivo JSON.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Criar um produto**: Permite adicionar um novo produto ao estoque. Você precisa fornecer o nome, o preço e a quantidade do produto. Os dados são armazenados no arquivo JSON e o produto é adicionado ao estoque.

2. **Atualizar um produto**: Permite atualizar as informações de um produto existente no estoque. Você precisa fornecer o nome do produto e, em seguida, pode atualizar o preço e a quantidade. Os dados são atualizados no arquivo JSON.

3. **Excluir um produto**: Permite excluir um produto do estoque. Você precisa fornecer o nome do produto. Se o produto existir no estoque, ele será removido do arquivo JSON.

4. **Exibir o estoque**: Mostra os produtos atualmente disponíveis no estoque. O nome, preço e quantidade de cada produto são exibidos na tela.

5. **Vender um produto**: Permite vender um produto do estoque. Você precisa fornecer o nome do produto e a quantidade a ser vendida. Se houver quantidade suficiente do produto disponível no estoque, a quantidade vendida será deduzida do estoque e os dados serão atualizados no arquivo JSON.

6. **Sair**: Encerra o programa.

## Como usar

1. Certifique-se de ter o Python instalado em seu ambiente.

2. Faça o download dos arquivos do projeto.

3. Abra o terminal e navegue até o diretório onde os arquivos do projeto estão localizados.

4. Execute o seguinte comando para iniciar o programa: python pdv.py

5. No menu principal, escolha uma das opções digitando o número correspondente.

6. Siga as instruções fornecidas para realizar as ações desejadas.

7. Para sair do programa, escolha a opção "6. Sair".

## Dependências

O projeto não possui dependências externas. A biblioteca `json` é utilizada para manipulação de arquivos JSON, mas já está incluída na biblioteca padrão do Python.

## Armazenamento de Dados

Os dados do estoque são armazenados em um arquivo JSON chamado `stock_data.json`. Se o arquivo não existir, será criado automaticamente ao adicionar o primeiro produto. Caso contrário, o programa carrega os dados do arquivo JSON existente no início e salva as alterações no arquivo ao adicionar, atualizar ou excluir produtos.

---
