# Gramática Independente de Contexto

## Autor

**Nome:** João Coelho

**Número:** A100596

## Resumo

Este trabalho consiste na implementação de uma gramática livre de contexto para representar expressões aritméticas e lógicas simples. A gramática é definida por um conjunto de terminais, não-terminais e produções, que descrevem como as expressões podem ser formadas. 

### Exemplos de Expressões

```
$ ?a
$ b=a*2/(27-3)
$ !a+b
$ c=(a*b)/(a/b)
```

## Resolução

```
T = {'?', '!', '(', ')', '=', '*', '/', '-', '+', var, num}

N = {S, Expr, Expr2, Expr3, Op, Op2}

S = S

P = {
    
    S -> '?' var            LA = {'?'}
       | '!' Expr           LA = {'!'}  
       | var '=' Expr       LA = {var} 

    Expr -> Expr2 Op

    Op -> '+' Expr          LA = {'+'}
        | '-' Expr          LA = {'-'}               
        | &                 LA = {$, ')'}
    
    Expr2 -> Expr3 Op2      LA = {'(', var, num}

    Op2 -> '*' Expr         LA = {'*'}
         | '/' Expr         LA = {'/'}
         | &                LA = {'+', '-', $, ')'}
    
    Expr3 -> '(' Expr ')'   LA = {'('}
           | var            LA = {var}
           | num            LA = {num}
}
```