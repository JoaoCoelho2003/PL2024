# TPC1: Análise de um dataset

## Autor

**Nome:** João Coelho

**id:** A100596

## Resumo

1. Começo por ler o ficheiro **.csv** a partir do **stdin**;
2. A verificação das modalidades presentes no ficheiro é realizada a partir de uma observação global das linhas do ficheiro, guardando numa lista as novas modalidades encontradas;
3. Para verificar a percentagem de atletas aptos e não aptos, foi verificada cada linha do ficheiro e, por cada True ou False na respetiva coluna, foi incrementado o valor nas variáveis usadas para guardar o número de atletas de cada categoria. No final foi calculada a percentagem.
4. Por fim, para a distribuição dos atletas pelas idades, criei uma array de **ints** e, ao percorrer os dados, divido a idade do mesmo por 5 e incremento 1 na posição equivalente ao resultado obtido na divisão. De seguida, calculo as percentagens para a distribuição.
