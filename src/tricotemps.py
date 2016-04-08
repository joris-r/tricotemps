#!/usr/bin/env python3

import ply.lex as lex
import sys

tokens = (
    'SIGIL',
    'DIESE',
    'STRING',
    'NUM',
    'YEAR_FR',
    'WEEK_FR',
    'DAYS_FR',
)


t_SIGIL = r'@'
t_DIESE = r'\#'
t_NUM = r'[0-9]+'
t_YEAR_FR = r'Année'
t_WEEK_FR = r'Semaine'
t_DAYS_FR = r'j'
t_STRING = r'"[^"]*"'

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

t_ignore = ' \r\t'

def t_error(t):
    print('Illegal character {}'.format(t.value[0]))
    exit(1)

def goGoGo(source):
    lexer = lex.lex()
    lexer.input(source)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)




if __name__ == "__main__":
    with open(sys.argv[1], 'r') as source:
        goGoGo(source.read())


