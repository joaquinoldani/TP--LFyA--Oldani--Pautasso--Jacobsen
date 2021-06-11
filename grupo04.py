try:
    import ply.lex as lex
    import ply.yacc as yacc        
except ImportError:
    raise ImportError('Please, add ply library to the root of the proyect or run pip install -r requirements.txt')

# Initialization
columns = []
tables = []

reserved = {
    'AND': 'AND',
    'AS': 'AS',
    'ASC': 'ASC',
    'BY': 'BY',
    'COUNT': 'COUNT',
    'CONTIDION': 'CONTIDION',
    'DESC': 'DESC',
    'DISTINCT': 'DISTINCT',
    'FROM': 'FROM',
    'FULL': 'FULL',
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
    'OUTER': 'OUTER',
    'RIGHT': 'RIGHT',
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
    'NUMBER',
    'QUOTE'
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
t_QUOTE = r'\''

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

lexer = lex.lex()

def p_QUERY_AXIOM(p):
    '''QUERY : SELECT_NT FROM_NT JOIN_NT WHERE_NT GROUP_BY_NT ORDER_BY_NT'''

def p_SELECT(p):
    '''SELECT_NT : SELECT DISTINCT COLUMNS
                 | SELECT COLUMNS'''

def p_COLUMNS(p):
    '''COLUMNS : COLUMN COMMA COLUMNS
               | DISTINCT COLUMN COMMA COLUMNS
               | COLUMN''' 

def p_ALIAS(p):
    '''ALIAS : AS QUOTE STRING QUOTE
             | AS QUOTE STRING STRINGS QUOTE
             | AS STRING'''

def p_STRINGS(p):
    '''STRINGS : STRING STRINGS
               | STRING''' 

def p_COLUMN(p):
    '''COLUMN : COLUMN_WIHTOUT_ALIAS
              | STRING DOT STRING ALIAS
              | FUNCTION ALIAS
              | FUNCTION'''
    if len(p) == 4 or len(p) == 5:
        column = { 'column_name' : p[3], 'table_alias' : p[1] }
        if column is not None and column not in columns:
            columns.append(column)

def p_COLUMN_WIHTOUT_ALIAS(p):
    '''COLUMN_WIHTOUT_ALIAS : STRING DOT STRING'''
    if len(p) == 4:
        column = { 'column_name' : p[3], 'table_alias' : p[1] }
    if column is not None and column not in columns:
        columns.append(column)
    
def p_FUNCTION(p):
    '''FUNCTION : VALID_FUNCTIONS LEFT_PARENTHESIS COLUMN_WIHTOUT_ALIAS RIGHT_PARENTHESIS'''

def p_VALID_FUNCTIONS(p):
    '''VALID_FUNCTIONS : COUNT
                       | MAX
                       | MIN'''

def p_FROM(p):
    '''FROM_NT : FROM TABLES'''

def p_TABLES(p):
    '''TABLES : TABLE
              | TABLE COMMA TABLES'''

def p_TABLE(p):
    '''TABLE : STRING STRING
             | STRING AS STRING'''
    table = None
    if len(p) == 4:
        table = { 'table_name' : p[1], 'table_alias' : p[3] }
    if len(p) == 3:
        table = { 'table_name' : p[1], 'table_alias' : p[2] }
    if table is not None and table not in tables:
        tables.append(table)

def p_JOIN_NT(p):
    '''JOIN_NT : VALID_JOINS
                | '''

def p_VALID_JOINS(p):
    '''VALID_JOINS : VALID_JOIN
                   | VALID_JOIN VALID_JOINS'''

def p_VALID_JOIN(p):
    '''VALID_JOIN : INNER JOIN TABLE ON CONDITION
                   | LEFT JOIN TABLE ON CONDITION
                   | RIGHT JOIN TABLE ON CONDITION
                   | FULL OUTER JOIN TABLE ON CONDITION'''

def p_CONDITIONS(p):
    '''CONDITIONS : CONDITION
                  | CONTIDION CONDITIONS'''

def p_CONDITION(p):
    '''CONDITION : COLUMN_WIHTOUT_ALIAS COMPARATION_OPERATOR COLUMN_WIHTOUT_ALIAS
                 | COLUMN_WIHTOUT_ALIAS COMPARATION_OPERATOR FUNCTION
                 | COLUMN_WIHTOUT_ALIAS COMPARATION_OPERATOR QUOTE STRING QUOTE
                 | COLUMN_WIHTOUT_ALIAS COMPARATION_OPERATOR NUMBER'''

def p_COMPARATION_OPERATOR(p):
    '''COMPARATION_OPERATOR : EQUAL
                            | NOT_EQUAL
                            | GREATER_THAN
                            | GREATER_THAN_OR_EQUALS
                            | LESS_THAN
                            | LESS_THAN_OR_EQUALS'''

def p_WHERE_NT(p):
    '''WHERE_NT : WHERE COMPARATIONS
                | '''

def p_COMPARATIONS(p):
    '''COMPARATIONS : CONDITION
                    | CONDITION AND COMPARATIONS'''

def p_GROUP_BY_NT(p):
    '''GROUP_BY_NT : GROUP BY_NT
                    | '''

def p_BY_NT(p):
    '''BY_NT : BY COLUMNS
          | BY COLUMNS HAVING FUNCTION COMPARATION_OPERATOR STRING
          | BY COLUMNS HAVING FUNCTION COMPARATION_OPERATOR NUMBER'''

def p_ORDER_BY_NT(p):
    '''ORDER_BY_NT : ORDER BY_NT_WITHOUT_HAVING
                    | '''

def p_BY_NT_WITHOUT_HAVING(p):
    '''BY_NT_WITHOUT_HAVING : BY COLUMNS DESC
                            | BY COLUMNS ASC
                            | BY COLUMNS'''

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

def parse_select_statement(s):
    columns.clear()
    tables.clear()
    
    # Check if the tokens are valid.
    lexer = lex.lex()
    lexer.input(s)
    
    parser = yacc.yacc()
    parser.parse(s)

    diccionary = {}

    for table in tables:
        diccionary[table.get('table_name')] = []

        for column in columns:
            if column.get('table_alias') == table.get('table_alias'):
                diccionary[table.get('table_name')].append(column.get('column_name'))
                diccionary[table.get('table_name')].sort()
    return diccionary