import re
import sys
import ply.lex as ply

"""
def tokenize(code):
    token_specification = [
        ('SELECT', r'select'),
        ('FROM', r'from'),
        ('WHERE', r'where'),
        ('ID', r'[_A-Za-z]\w*'),
        ('COMMA', r','),
        ('OP', r'>='),
        ('NUM', r'\d+(\.\d+)?'),
        ('SKIP', r'[ \t]+'),
        ('ERRO', r'.'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    recognized = []
    mo = re.finditer(tok_regex, code, re.IGNORECASE)
    for m in mo:
        dic = m.groupdict()
        if dic['SELECT']:
            t = ("SELECT", dic['SELECT'], m.span())
        elif dic['FROM']:
            t = ("FROM", dic['FROM'], m.span())
        elif dic['WHERE']:
            t = ("WHERE", dic['WHERE'], m.span())
        elif dic['ID']:
            t = ("ID", dic['ID'], m.span())
        elif dic['COMMA']:
            t = ("COMMA", dic['COMMA'], m.span())
        elif dic['OP']:
            t = ("OP", dic['OP'], m.span())
        elif dic['NUM']:
            t = ("NUM", dic['NUM'], m.span())
        elif dic['SKIP']:
            continue
        else:
            t = ("ERRO", m.group(), m.span())
        recognized.append(t)

    return recognized
"""

# main SQL tokens
reserved = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE'
}

tokens = [
    'FIELD',
    'INSTRUCTION',
    'OPERATOR',
    'NUMBER',
    'COMMA'
] + list(reserved.values())

def t_INSTRUCTION(t):
    r'\b[a-zA-z]+\b'
    value = t.value.lower()
    t.type = reserved.get(value, 'FIELD') if value in reserved else 'FIELD'
    return t

def t_OPERATOR(t):
    r'[><=]+'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    return t

def t_COMMA(t):
    r','
    return t

t_ignore = ' \t'

def t_error(t):
    sys.stderr.write(f"Illegal character {t.value[0]}\n")
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def main():
    lexer = ply.lex()
    for line in sys.stdin:
        lexer.input(line)
        for tok in lexer:
            print(tok)

if __name__ == "__main__":
    main()