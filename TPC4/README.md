# Analisador Léxico

## Autor

**Nome:** João Coelho

**Número:** A100596

## Resumo

Neste trabalho foi implementado, em Python, um analisador léxico para instruções `SELECT..FROM` de SQL . O analisador é capaz de reconhecer diferentes partes de uma instrução SQL, como os comandos `SELECT`, `FROM` e `WHERE`, identificadores de tabelas e colunas, operadores, números e outros caracteres. Foi utilizado o conceito de expressões regulares para realizar o reconhecimento dos tokens.

## Resolução

1. **Especificação de Tokens**: Uma lista de especificações de token foi definida, onde cada especificação consiste numa tupla `(nome_do_token, padrão_regex)`. Os tokens especificados incluem:
    - `SELECT`: Correspondente à palavra-chave "select".
    - `FROM`: Correspondente à palavra-chave "from".
    - `WHERE`: Correspondente à palavra-chave "where".
    - `ID`: Correspondente a identificadores (nomes de tabelas, nomes de colunas, etc.), que devem começar com uma letra ou sublinhado, seguidos de letras, dígitos, etc.
    - `COMMA`: Correspondente a uma vírgula.
    - `GREATER`: Correspondente ao operador maior ou igual a (">=").
    - `NUM`: Correspondente a números, incluindo números inteiros e decimais.
    - `SKIP`: Ignora caracteres de espaço em branco (espaços e tabulações).
    - `ERRO`: Correspondente a qualquer outro caractere.

2. **Correspondência de Expressões Regulares**: Um padrão de expressão regular é construído pela junção das especificações de token usando o operador `|` (OR). De seguida, a função `re.finditer()` é utilizada para encontrar todas as correspondências das especificações de token na string de entrada.

3. **Tokenização**: Para cada correspondência encontrada por `re.finditer()`, o script determina o token correspondente com base no grupo correspondido na expressão regular. Ele constrói uma tupla `(tipo_do_token, valor_do_token, intervalo)` representando o tipo de token, o seu valor e o intervalo (índices de início e fim) na string de entrada.

4. **Saída**: O script coleta todos os tokens reconhecidos numa lista e imprime cada token, juntamente com seu tipo, valor e intervalo.

## Instruções de uso

Para usufruir das funcionalidades apresentadas é necessário correr o comando apresentado abaixo, substituindo *example.txt* pelo ficheiro que pretende analisar:

`cat example.txt | python3 resolucao.py`

Para além disso, também é possível executar apenas o *script python* e inserir a linha SQL que pretende analisar no *stdin*.