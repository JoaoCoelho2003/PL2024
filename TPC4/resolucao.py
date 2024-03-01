import re
import sys

def tokenize(code):
    token_specification = [
        ('SELECT', r'select'),
        ('FROM', r'from'),
        ('WHERE', r'where'),
        ('ID', r'[_A-Za-z]\w*'),
        ('COMMA', r','),
        ('GREATER', r'>='),
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
        elif dic['GREATER']:
            t = ("GREATER", dic['GREATER'], m.span())
        elif dic['NUM']:
            t = ("NUM", dic['NUM'], m.span())
        elif dic['SKIP']:
            continue
        else:
            t = ("ERRO", m.group(), m.span())
        recognized.append(t)

    return recognized

def main():
    for line in sys.stdin:
        tokens = tokenize(line)
        for token in tokens:
            print(token)

if __name__ == "__main__":
    main()