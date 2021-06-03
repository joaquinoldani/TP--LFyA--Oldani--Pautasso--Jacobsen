import sys

try:
    import ply.lex as lex
    import ply.yacc as yacc        
except ImportError:
    raise ImportError('Please, add ply library to the root of the proyect or run pip install -r requirements.txt')

reserved = {
    'AND': 'AND',
    'AS': 'AS',
    'ASC': 'ASC',
    'BY': 'BY',
    'COUNT': 'COUNT',
    'DESC': 'DESC',
    'DISTINCT': 'DISTINCT',
    'FROM': 'FROM',
    'GROUP': 'GROUP',
    'HAVING': 'HAVING',
    'INNER': 'INNER',
    'JOIN': 'JOIN',
    'LEFT': 'LEFT',
    'MAX': 'MAX',
    'MIN': 'MIN',
    'NULL': 'NULL',
    'ON': 'ON',
    'OR': 'OR',
    'ORDER': 'ORDER',
    'SELECT': 'SELECT',
    'WHERE': 'WHERE',
}

tokens = list(reserved.values()) + [
    'EQUAL', 
    'NOT_EQUAL',
    'GREATER_THAN',
    'GREATER_THAN_OR_EQUALS',
    'LESS_THAN',
    'LESS_THAN_OR_EQUALS',
    'RIGHT_PARENTHESIS',
    'RIGHT_BRACKET',
    'LEFT_PARENTHESIS',
    'LEFT_BRACKET',
    'COMMA',
    'DOT',
    'STRING',
    'NUMBER'
]

# Regular expressions for special tokens.
t_EQUAL = r'\='
t_NOT_EQUAL = r'\<>'
t_GREATER_THAN = r'\>'
t_GREATER_THAN_OR_EQUALS = r'\>='
t_LESS_THAN = r'\<'
t_LESS_THAN_OR_EQUALS = r'\<='
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_COMMA = r'\,'
t_DOT = r'\.'

## Token could be a string, a number or a new line and a string-token can't start with number in SQL and in the most common languages.

def t_STRING(t):
    ## A string-token can't start with number in SQL and in the most common languages
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    #r'\w'
    t.type = reserved.get(t.value, 'STRING')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore whitespace
t_ignore = ' \t'

# Error handler
def t_error(t):
    print("Lex error. Character '%s' is not valid" % t.value[0])
    t.lexer.skip(1)

query = """SELECT p.Nombre,
	p.Apellido,
	p.Email,
	s.CodigoSocio,
	a.CodigoAlquiler,
	j.Nombre as 'Nombre juego',
	a.FechaRetiro,
	a.FechaDevolucion,
	a.CostoPorDia, 
	ac.Costo, 
	ac.EstadoPago, 
	ac.FechaPago,
	s.Saldo as 'deuda total'
	FROM dbo.AlquileresCosto ac, dbo.Alquileres a, dbo.Socios s, dbo.Personas p, dbo.Juegos j
	WHERE a.CodigoSocio = s.CodigoSocio
	AND s.CodigoPersona = p.CodigoPersona
	AND a.CodigoAlquiler = ac.CodigoAlquiler
	AND j.CodigoJuego = a.CodigoJuego
    GROUP BY p.apellido
    ORDER BY p.Apellido DESC"""

# Check if the tokens are valid.
lexer = lex.lex()
lexer.input(query)

# For real use 
# lexer.input(sys.argv[1:])

## Print the tokens
while True:
    tok = lexer.token()
    if not tok:
        break 
    print(tok)

## Check if query has valid sintax.
parser = yacc.yacc()

# parser.input(sys.argv[1:])

while True:
    try:
        s = input(query)
    except EOFError:
        break
    if not s:
        continue
    parser.parse(s)

