# Simulador de Máquina de Vendas

## Autor

**Nome:** João Coelho

**Número:** A100596

## Resumo

Este programa, desenvolvido em Python, simula o comportamento de uma máquina de vendas. Ele permite que os utilizadores interajam com a máquina inserindo comandos para listar produtos, adicionar moedas, selecionar produtos para compra e sair do mesmo.

## Resolução

Tal como foi referido anteriormente, o programa foi desenvolvido em Python, aproveitando a biblioteca `ply` para realizar análise léxica e interpretar os comandos fornecidos pelo utilizador. Aqui está uma explicação mais detalhada das técnicas e conceitos utilizados:

### Análise Léxica com PLY

- **Tokens:** Definimos os tokens que representam os diferentes tipos de entrada que o programa pode receber, como `LISTAR`, `MOEDA`, `SELECIONAR` e `SAIR`.
- **Expressões Regulares:** Utilizamos expressões regulares para definir padrões de correspondência para cada tipo de token, permitindo identificar e classificar corretamente as entradas do utilizador.
- **Funções de Tokenização:** Implementamos funções de tokenização que definem como cada tipo de entrada deve ser processado e convertido em tokens reconhecidos pelo programa.

### Interação com o Utilizador

- **Entrada de Comandos:** O programa aguarda a entrada do utilizador por meio do terminal, onde ele pode inserir os comandos desejados para interagir com a máquina de vendas.
- **Processamento de Comandos:** Cada comando fornecido pelo utilizador é interpretado e executado pelo programa, permitindo listar produtos, adicionar moedas, selecionar produtos para compra e sair da simulação.
- **Feedback ao utilizador:** O programa fornece feedback ao utilizador em cada etapa da interação, informando sobre o status da operação realizada e fornecendo detalhes relevantes, como troco e disponibilidade de produtos.

### Manipulação de Dados do Produto

- **Formato de Dados:** Os dados dos produtos são fornecidos a partir de um ficheiro JSON, seguindo uma estrutura específica que inclui o ID do produto, o nome e o preço.
- **Carregamento de Dados:** O programa carrega os dados do produto a partir do ficheiro JSON e organiza-os numa estrutura de dados adequada para facilitar o acesso e manipulação durante a simulação da máquina de vendas.

### Manipulação de Saldo e Troco

- **Controle de Saldo:** O programa mantém o controle do saldo do utilizador, atualizando-o conforme moedas são adicionadas e produtos são comprados.
- **Cálculo de Troco:** Ao sair da simulação, o programa calcula o troco a ser devolvido ao utilizador, utilizando algoritmos para determinar as combinações mais eficientes de moedas para minimizar o número de moedas devolvidas.

## Instruções de Uso


Execute o programa a partir do terminal ou prompt de comando, fornecendo o arquivo JSON como argumento.

```
python3 script.py vendingMachine.json
```

### Lista de Comandos

- **LISTAR:** Exibir todos os produtos na máquina de vendas.
- **MOEDA:** Adicionar moedas à máquina.
- **SELECIONAR:** Selecionar um produto para compra.
- **SAIR:** Sair da simulação e receber troco.

## Exemplo de Uso

```
$ MOEDA 1e,20c,50c
$ 1e70c
$ SELECIONAR 8
$ You do not have enough money
$ SELECIONAR 2
$ Change: 70c
$ MOEDA 20c
$ 0e90c
$ listar
$ ID | NAME | PRICE
$ 1 | Water | 50c
$ 2 | Soda | 1e
$ 3 | Snack | 1e20c
$ 4 | Chocolate Bar | 80c
$ 5 | Coffee | 55c
$ 6 | Tea | 1e20c
$ 7 | Juice | 1e20c
$ 8 | Sandwich | 2e10c
$ 9 | Chips | 1e20c
$ 10 | Candy | 70c
$ SELECIONAR 10   
$ Change: 20c
$ moeda 1e,1c,5c
$ 1e26c
$ SAIR
$ Change: 126c
$ 1e 20c 5c 1c
```



