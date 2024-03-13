# Simulador de Máquina de Vendas

## Autor

**Nome:** João Coelho

**Número:** A100596

## Resumo

Este programa, desenvolvido em Python, simula o comportamento de uma máquina de vendas. Ele permite que os utilizadores interajam com a máquina inserindo comandos para listar produtos, adicionar moedas, adicionar produtos/stock, selecionar produtos para compra e sair do mesmo.

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

### Manipulação de Saldo, Troco e Stock

- **Controlo de Saldo:** O programa mantém o controlo do saldo do utilizador, atualizando-o conforme moedas são adicionadas e produtos são comprados.
- **Controlo de Stock:** Existe um controlo do stock dos produtos, que é atualizado sempre que alguma compra é realizada, ou há algum tipo de reabastecimento dos produtos da máquina.
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
- **ADICIONAR:** Adicionar um novo produto à máquina(ou stock).
- **SAIR:** Sair da simulação e receber troco.

## Exemplo de Uso

```
$ listar
$      Number          |            Name                               |       Stock          |    Price    
$         1            |        Water                                  |        5             |        50c  
$         2            |        Soda                                   |        2             |        1e   
$         3            |        Snack                                  |        1             |        1e20c
$         4            |        Chocolate Bar                          |        3             |        80c  
$         5            |        Coffee                                 |        4             |        55c  
$         6            |        Tea                                    |        2             |        1e20c
$         7            |        Juice                                  |        1             |        1e20c
$         8            |        Sandwich                               |        7             |        2e10c
$         9            |        Chips                                  |        3             |        1e20c
$         10           |        Candy                                  |        5             |        70c  
$ moeda 2e,2e,2e,2e,2e
$ 10e00c
$ selecionar 2
$ Change: 9e00c
$ selecionar 1
$ Change: 8e50c
$ selecionar 7
$ Change: 7e30c
$ selecionar 7
$ Product not available. Out of stock
$ selecionar 8
$ Change: 5e20c
$ selecionar 8
$ Change: 3e10c
$ selecionar 8
$ Change: 1e00c
$ selecionar 8
$ You do not have enough money
$ adicionar Water 5 
$ Product Water added to the machine
$ adicionar IceTea 10 1e20c
$ Product IceTea added to the machine
$ listar
$      Number          |            Name                               |       Stock          |    Price    
$         1            |        Water                                  |        9             |        50c  
$         2            |        Soda                                   |        1             |        1e   
$         3            |        Snack                                  |        1             |        1e20c
$         4            |        Chocolate Bar                          |        3             |        80c  
$         5            |        Coffee                                 |        4             |        55c  
$         6            |        Tea                                    |        2             |        1e20c
$         7            |        Juice                                  |        0             |        1e20c
$         8            |        Sandwich                               |        4             |        2e10c
$         9            |        Chips                                  |        3             |        1e20c
$         10           |        Candy                                  |        5             |        70c  
$         11           |        IceTea                                 |        10            |        1e20c
$ sair
$ Change: 1e00c
$ 1e
```




