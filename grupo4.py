import ply

entrada = ['num', '+', 'num', '$']

def yylex(entrada_actual):
    look = entrada_actual[0]
    entrada_actual = entrada_actual[1:]
    return look, entrada_actual

NT = ['T', 'T1', 'E', 'E1', 'F']

table = {
    'E': {'num': ['T', 'E1'], '(': ['T', 'E1'], '$': ['OK']},
    'E1': {'+': ['+', 'T', 'E1'], '-': ['-', 'T', 'E1'], ')': [], '$': []},
    'T': {'num': ['F', 'T1'], '(': ['F', 'T1']},
    'T1': {'+': [], '-': [], '*': ['*', 'F', 'T1'], '/': ['*', 'F', 'T1'], ')': [], '$': []},
    'F': {'num': ['num'], '(': ['(', 'E', ')'], }
}

stack = ['E']
look, entrada = yylex(entrada)
i = 0
while stack:
    i += 1
    input()
    print(f'''Iteración {i}:
            - Pila: {stack}
            - Entrada actual: {entrada}
            - Look: {look}''')
    s = stack.pop()
    if s in NT:
        l = table[s][look]
        l = l[::-1]
        stack.extend(l)
    elif s == look:
        look, entrada = yylex(entrada)
    else:
        print('Error')

if look == '$':
    print('OK')
else:
    print('Error')
input()