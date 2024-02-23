# Somatório de Números num Ficheiro

## Autor

**Nome:** João Coelho

**Número:** A100596

## Resumo

Neste trabalho foi desenvolvido um *script python* que é responsável por definir o comportamento de um incrementador de números num ficheiro de texto, este somatório segue um conjunto de regras, definidas a seguir:

1. Quando a palavra **on** é encontrada no texto, qualquer número que aparecer de seguida é incrementado a uma variável;
2. Quando a palavra **off** é encontrada no texto, os números subsequentes não são considerados;
3. Ao encontrar a string "=", o valor da variável é devolvido e o programa é encerrado.
4. As palavras "on" e "off" podem ser encontradas em qualquer combinação de letras maiúsculas e minúsculas, e até mesmo dentro de outras palavras.

## Resolução

1. Tenho duas variáveis booleanas responsáveis por determinar se *on* e *off* estão ativos;
1. São utilizadas expressões regulares e funções do *módulo re* para encontrar ocurrências das strings alvo;
2. Se uma das strings (on | off) fôr encontrada então as variáveis booleanas são alteradas para refletir tal facto;
3. Dependendo do valor dessas mesmas variáveis, o valor dos inteiros encontrados, também possível graças ao uso de expressões regulares, será incrementado ao counter ou não;
4. Por fim, como foi referido anteriormente, caso a string "=" seja encontrada, o valor do counter é retornado e o programa termina.

## Instruções de uso

Para usufruir das funcionalidades apresentadas é necessário correr o comando apresentado abaixo, substituindo *example.txt* pelo ficheiro que pretende analisar:

**cat example.txt | python3 resolucao.py**