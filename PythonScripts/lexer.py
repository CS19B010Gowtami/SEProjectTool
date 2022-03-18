from ast import keyword
import ply.lex as lex

# DROP, USE and SHOW are not required ig
# if both lower case and uppercase are allowed for keywords we need to be map 'add' to 'ADD' ; 'constraint' to 'CONSTRAINT' etc
keywords = {
	'ADD'  :  'ADD',
	'CONSTRAINT'  :  'CONSTRAINT',
    'ALTER'  :  'ALTER',
	'COLUMN'  :  'COLUMN',
	'TABLE'  :  'TABLE',
	'AS'  :  'AS',
	'ASC'  :  'ASC',
	'BACKUP'  :  'BACKUP',
	'DATABASE'  :  'DATABASE',
	'CASE'  :  'CASE',
	'CHECK'  :  'CHECK',
	'CREATE'  :  'CREATE',
	'INDEX'  :  'INDEX',
	'REPLACE'  :  'REPLACE',
	'VIEW'  :  'VIEW',
	'PROCEDURE'  :  'PROCEDURE',
	'UNIQUE'  :  'UNIQUE',
	'DEFAULT'  :  'DEFAULT',
	'DELETE'  :  'DELETE',
	'DESC'  :  'DESC',
	'DISTINCT'  :  'DISTINCT',
	'DROP'  :  'DROP',
	'USE'  :  'USE',
	'SHOW'  :  'SHOW',
	'EXEC'  :  'EXEC',
	'FOREIGN'  :  'FOREIGN',
	'KEY'  :  'KEY',
	'FROM'  :  'FROM',
	'FULL'  :  'FULL',
	'OUTER'  :  'OUTER',
	'JOIN'  :  'JOIN',
	'GROUP'  :  'GROUP',
	'BY'  :  'BY',
	'HAVING'  :  'HAVING',
	'INNER'  :  'INNER',
	'INSERT'  :  'INSERT',
	'INTO'  :  'INTO',
	'SELECT'  :  'SELECT',
	'NULL'  :  'NULL',
	'IS'  :  'IS',
	'LEFT'  :  'LEFT',
	'LIMIT'  :  'LIMIT',
	'ORDER'  :  'ORDER',
	'PRIMARY'  :  'PRIMARY',
	'RIGHT'  :  'RIGHT',
	'ROWNUM'  :  'ROWNUM',
	'TOP'  :  'TOP',
	'SET'  :  'SET',
	'TRUNCATE'  :  'TRUNCATE',
	'UNION'  :  'UNION',
	'UPDATE'  :  'UPDATE',
	'VALUES'  :  'VALUES',
	'WHERE'  :  'WHERE',
	'VARCHAR' : 'VARCHAR',

	'ALL'  :  'ALL',
	'AND'  :  'AND',
	'ANY'  :  'ANY',
	'BETWEEN'  :  'BETWEEN',
	'EXISTS'  :  'EXISTS',
	'IN'  :  'IN',
	'LIKE'  :  'LIKE',
	'NOT'  :  'NOT',
	'OR'  :  'OR',
	'SOME'  :  'SOME'
}

tokens = [
	'REALNUM',
	'INTNUM',
	'STRING',
	'CHARACTER',
	'IDENTIFIER',
	'EQUAL',
	'ADDEQ',
	'SUBEQ',
	'MULEQ',
	'DIVEQ',
	'MODEQ',
	'GTEQ',
	'LTEQ',
	'NOTEQ',
	'ANDEQ',
	'OREQ',
	'EXLUSIVE_EQ',
	'ADDOP',
	'SUBOP',
	'MULOP',
	'DIVOP',
	'MODOP',
	'GTOP',
	'LTOP',
	'ANDOP',
	'OROP',
	'EXLUSIVE_OP',
	'SEPARATORS',
	'SEMICOLON',
	'LCB',
	'RCB',
	'LFB',
	'RFB',
	'LSB',
	'RSB'
] + list(keywords.values())

t_EQUAL = r'\='

# Arithmetic Assignment Operators
t_ADDEQ = r'\+\='
t_SUBEQ = r'\-\='
t_MULEQ = r'\*\='
t_DIVEQ = r'\/\='
t_MODEQ = r'\%\='

# Comparison Operators
t_GTEQ = r'\>\='
t_LTEQ = r'\<\='
t_NOTEQ = r'\<\>'

# Bitwise Assignment Operators
t_ANDEQ = r'\&\='
t_OREQ = r'\|\='
t_EXLUSIVE_EQ = r'\^\='

# Arithmetic Operators
t_ADDOP = r'\+'
t_SUBOP = r'\-'
t_MULOP = r'\*'
t_DIVOP = r'\/'
t_MODOP = r'\%'

# Comparison Operators
t_GTOP = r'\>'
t_LTOP = r'\<'

# Bitwise Operators
t_ANDOP = r'\&'
t_OROP = r'\|'
t_EXLUSIVE_OP = r'\^'

t_SEPARATORS = r'\,'
t_SEMICOLON = r'\;'
t_LCB = r'\('
t_RCB = r'\)'
t_LFB = r'\{'
t_RFB = r'\}'
t_LSB = r'\['
t_RSB = r'\]'

t_ignore = r' |\\\t'

# Identifier refers to table name, attribute name etc
def t_IDENTIFIER(t):
	r'[a-zA-Z]+'
	t.type = keywords.get(t.value, 'IDENTIFIER')
	return t

# String refers to attribute value which may be composed of a character(s)
def t_STRING(t):
	r'\'(\s|\S)+\''
	l = len(t.value)
	t.value = t.value[1:(l-1)]
	try:
		t.value = int(t.value)
		t.type = 'INTNUM'
	except ValueError:
		t.value = float(t.value)
		t.type = 'REALNUM'
	finally:
		t.type = 'STRING'	
	return t

def t_REALNUM(t):
	r'\d+.\d+'
	t.value = float(t.value)
	return t

def t_INTNUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

# Updating line number for the tokens
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

lexer = lex.lex()
test = '''

'''

lexer.input(test)
# tok consists of attributes tok.type, tok.value, tok.lineno, and tok.lexpos
while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)