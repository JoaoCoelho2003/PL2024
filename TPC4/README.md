# Analisador Léxico

## Autor

**Nome:** João Coelho  
**Número:** A100596

## Resumo

Neste trabalho, foi implementado um analisador léxico em Python para instruções SQL `SELECT..FROM`. O analisador reconhece diferentes partes de uma instrução SQL, como os comandos `SELECT`, `FROM` e `WHERE`, identificadores de tabelas e colunas, operadores, números e outros caracteres. Este analisador utiliza a biblioteca Ply para definir os tokens e realizar a tokenização do input.

## Resolução

1. **Especificação de Tokens**: As especificações de tokens são definidas utilizando expressões regulares. Cada token é definido com um padrão de expressão regular correspondente ao seu tipo, como `SELECT`, `FROM`, `WHERE`, `FIELD`, `COMMA`, `OPERATOR` e `NUM`.

2. **Tokenização com Ply**: As especificações de tokens são fornecidas à biblioteca Ply, que é responsável por tokenizar o input de acordo com essas regras. Ply gera um analisador léxico baseado nas especificações fornecidas.

3. **Identificação de Tokens**: O analisador léxico Ply lê o input linha por linha e identifica os tokens presentes em cada uma. Para cada token encontrado, o analisador retorna uma tupla contendo o tipo do token, o valor do token e o intervalo na linha em que o token foi encontrado.

4. **Saída dos Tokens**: Os tokens identificados são impressos no stdout, exibindo o tipo do token, o valor do token e o intervalo na linha.

## Instruções de uso

Para usar o analisador léxico, execute o seguinte comando no terminal, substituindo *example.txt* pelo nome do ficheiro que contém as instruções SQL que deseja analisar:

```
$ cat example.txt | python3 resolucao.py
```


Ou, se preferir, é possível executar o script Python diretamente e inserir as linhas SQL que deseja analisar no stdin.

## Exemplo de Uso

```
$ SELECT salario, nome, idade FROM trabalhadores WHERE salario >= 820
$ LexToken(SELECT,'SELECT',1,0)
$ LexToken(FIELD,'salario',1,7)
$ LexToken(COMMA,',',1,14)
$ LexToken(FIELD,'nome',1,16)
$ LexToken(COMMA,',',1,20)
$ LexToken(FIELD,'idade',1,22)
$ LexToken(FROM,'FROM',1,28)
$ LexToken(FIELD,'trabalhadores',1,33)
$ LexToken(WHERE,'WHERE',1,47)
$ LexToken(FIELD,'salario',1,53)
$ LexToken(OPERATOR,'>=',1,61)
$ LexToken(NUMBER,'820',1,64)
```
