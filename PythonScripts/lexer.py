from sly import Lexer

class MyLexer(Lexer):

    # these are set of tokens that are to be exported to the parser
    tokens = {
            "REALNUM",
			"INTNUM",
			"STRING",
			"CHARACTER",
		    "IDENTIFIER",
			"EQUAL",
			"ADDEQ",
			"SUBEQ",
			"MULEQ",
			"DIVEQ",
			"MODEQ",
			"GTEQ",
			"LTEQ",
			"NOTEQ",
			"ANDEQ",
			"OREQ",
			"EXLUSIVE_EQ",
			"SUBOP",
			"MULOP",
			"DIVOP",
			"MODOP",
			"GTOP",
			"LTOP",
			"ANDOP",
			"OROP",
			"EXLUSIVE_OP",
			"SEPARATORS",
			"SEMICOLON",
			"LCB",
			"RCB",
			"LFB",
			"RFB",
			"LSB",
            "NAMES"
			"RSB","UPDATE", "BACKUP", "FROM", "DISTINCT", "LIMIT", "ORDER", "ADD", "DATABASE", "BETWEEN", "ASC", "CASE", "EXISTS", "AND", "TRUNCATE", "PROCEDURE", "WHERE", "VALUES", "ALL", "HAVING", "LIKE", "EXEC", "CONSTRAINT", "COLUMN", "DEFAULT", "ROWNUM", "REPLACE", "IS", "SET", "LEFT", "AS", "FULL", "ALTER", "RIGHT", "GROUP", "INTO", "SHOW", "ANY", "NULL", "BY", "INSERT", "SELECT", "NOT", "TABLE", "KEY", "USE", "TOP", "UNION", "INNER", "CHECK", "JOIN", "FOREIGN", "PRIMARY", "IN", "UNIQUE", "VIEW", "DELETE", "OUTER", "VARCHAR", "OR", "INDEX", "DROP", "CREATE", "SOME", "DESC"
		}

    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    ID['ADD']  =  ADD
    ID['CONSTRAINT']  = CONSTRAINT
    ID['ALTER']  =  ALTER
    ID['COLUMN']  =  COLUMN
    ID['TABLE']  = TABLE
    ID['AS']  =  AS
    ID['ASC']  = ASC
    ID['BACKUP']  =  BACKUP
    ID['DATABASE']  =  DATABASE
    ID['CASE']  =  CASE
    ID['CHECK']  =  CHECK
    ID['CREATE']  =  CREATE
    ID['INDEX']  =  INDEX
    ID['REPLACE'] = REPLACE
    ID['VIEW'] = VIEW
    ID['PROCEDURE'] = PROCEDURE
    ID['UNIQUE'] = UNIQUE
    ID['DEFAULT'] = DEFAULT
    ID['DELETE'] = DELETE
    ID['DESC'] = DESC
    ID['DISTINCT'] = DISTINCT
    ID['DROP'] = DROP
    ID['USE'] = USE
    ID['SHOW'] = SHOW
    ID['EXEC'] = EXEC
    ID['FOREIGN'] = FOREIGN
    ID['KEY'] = KEY
    ID['FROM'] = FROM
    ID['FULL'] = FULL
    ID['OUTER'] = OUTER
    ID['JOIN'] = JOIN
    ID['GROUP'] = GROUP
    ID['BY'] = BY
    ID['HAVING'] = HAVING
    ID['INNER'] = INNER
    ID['INSERT'] = INSERT
    ID['INTO'] = INTO
    ID['SELECT'] = SELECT
    ID['NULL'] = NULL
    ID['IS'] = IS
    ID['LEFT'] = LEFT
    ID['LIMIT'] = LIMIT
    ID['ORDER'] = ORDER
    ID['PRIMARY'] = PRIMARY
    ID['RIGHT'] = RIGHT
    ID['ROWNUM'] = ROWNUM
    ID['TOP'] = TOP
    ID['SET'] = SET
    ID['TRUNCATE'] = TRUNCATE
    ID['UNION'] = UNION
    ID['UPDATE'] = UPDATE
    ID['VALUES'] = VALUES
    ID['WHERE'] = WHERE
    ID['VARCHAR'] = VARCHAR
    ID['ALL'] = ALL
    ID['AND'] = AND
    ID['ANY'] = ANY
    ID['BETWEEN'] = BETWEEN
    ID['EXISTS'] = EXISTS
    ID['IN'] = IN
    ID['LIKE'] = LIKE
    ID['NOT'] = NOT
    ID['OR'] = OR
    ID['SOME'] = SOME

    EQUAL = r'\='
    NAMES = r'[a-zA-Z_]*'
    COMMA = r'\,'
    # Arithmetic Assignment Operators
    ADDEQ = r'\+\='
    SUBEQ = r'\-\='
    MULEQ = r'\*\='
    DIVEQ = r'\/\='
    MODEQ = r'\%\='

    # Comparison Operators
    GTEQ = r'\>\='
    LTEQ = r'\<\='
    NOTEQ = r'\<\>'

    # Bitwise Assignment Operators
    ANDEQ = r'\&\='
    OREQ = r'\|\='
    EXLUSIVE_EQ = r'\^\='

    # Arithmetic Operators
    ADDOP = r'\+'
    SUBOP = r'\-'
    MULOP = r'\*'
    DIVOP = r'\/'
    MODOP = r'\%'

    # Comparison Operators
    GTOP = r'\>'
    LTOP = r'\<'

    # Bitwise Operators
    ANDOP = r'\&'
    OROP = r'\|'
    EXLUSIVE_OP = r'\^'

    SEPARATORS = r'\,'
    SEMICOLON = r'\;'
    LCB = r'\('
    RCB = r'\)'
    LFB = r'\{'
    RFB = r'\}'
    LSB = r'\['
    RSB = r'\]'

    ignore = '\t'

    @_(r'\d+')
    def INTNUM(self, t):
     t.value = int(t.value)
     return t

    @_(r'\d+.\d+')
    def REALNUM(self, t):
        t.value = float(t.value)
        return t

    @_(r'''("[^"\\]*(\\.[^"\\]*)*"|'[^'\\]*(\\.[^'\\]*)*')''')
    def STRING(self, t):
        t.value = self.remove_quotes(t.value)
        return t

    @_(r'\d+.\d+')
    def REALNUM(self, t):
        t.value = float(t.value)
        return t
    @_(r'\d+')
    def INTNUM(self, t):
        t.value = int(t.value)
        return t

    ignore_comment = r'\#.*'

	# Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

if __name__ == '__main__':
	data = '''
WHILE count <= 10
HAVING CREATE AS 
'''
	lexer = MyLexer()
	for tok in lexer.tokenize(data):
		print(tok)