from sly import Lexer

class MyLexer(Lexer):

    # these are set of tokens that are to be exported to the parser
    tokens = {
            "REALNUM",
			"INTNUM",
            "COL_NAME",
            "TABLE_NAME",
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
			"RSB","UPDATE", "BACKUP", "FROM", "DISTINCT", "LIMIT", "ORDER", "ADD", "DATABASE", "BETWEEN", "ASC", "CASE", "EXISTS", "AND", "TRUNCATE", "PROCEDURE", "WHERE", "VALUES", "ALL", "HAVING", "LIKE", "EXEC", "CONSTRAINT", "COLUMN", "DEFAULT", "ROWNUM", "REPLACE", "IS", "SET", "LEFT", "AS", "FULL", "ALTER", "RIGHT", "GROUP", "INTO", "SHOW", "ANY", "NULL", "BY", "INSERT", "SELECT", "NOT", "TABLE", "KEY", "USE", "TOP", "UNION", "INNER", "CHECK", "JOIN", "FOREIGN", "PRIMARY", "IN", "UNIQUE", "VIEW", "DELETE", "OUTER", "VARCHAR", "OR", "INDEX", "DROP", "CREATE", "SOME", "DESC","BOOL"
		}

    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ADD = r'ADD'
    CONSTRAINT = r'CONSTRAINT'  
    ALTER = r'ALTER'   
    COLUMN = r'COLUMN'  
    TABLE = r'TABLE' 
    AS = r'AS' 
    ASC = r'ASC' 
    BACKUP = r'BACKUP'  
    DATABASE = r'DATABASE' 
    CASE = r'CASE'  
    CHECK = r'CHECK' 
    CREATE = r'CREATE'  
    INDEX = r'INDEX'  
    REPLACE = r'REPLACE'
    VIEW = r'VIEW'
    PROCEDURE = r'PROCEDURE'
    UNIQUE = r'UNIQUE'
    DEFAULT = r'DEFAULT'
    DELETE = r'DELETE'
    DESC = r'DESC'
    DISTINCT = r'DISTINCT'
    DROP = r'DROP'
    USE = r'USE'
    SHOW = r'SHOW'
    EXEC = r'EXEC'
    FOREIGN = r'FOREIGN'
    KEY = r'KEY'
    FROM = r'FROM'
    FULL = r'FULL'
    OUTER = r'OUTER'
    JOIN = r'JOIN'
    GROUP = r'GROUP'
    BY = r'BY'
    HAVING = r'HAVING'
    INNER = r'INNER'
    INSERT = r'INSERT'
    INTO = r'INTO'
    SELECT = r'SELECT'
    NULL = r'NULL'
    IS = r'IS'
    LEFT = r'LEFT'
    LIMIT = r'LIMIT'
    ORDER = r'ORDER'
    PRIMARY = r'PRIMARY'
    RIGHT = r'RIGHT'
    ROWNUM = r'ROWNUM'
    TOP = r'TOP'
    SET = r'SET'
    TRUNCATE = r'TRUNCATE'
    UNION = r'UNION'
    UPDATE = r'UPDATE'
    VALUES = r'VALUES'
    WHERE = r'WHERE'
    VARCHAR = r'VARCHAR'
    ALL = r'ALL'
    AND = r'AND'
    ANY = r'ANY'
    BETWEEN = r'BETWEEN'
    EXISTS = r'EXISTS'
    IN = r'IN'
    LIKE = r'LIKE'
    NOT = r'NOT'
    OR = r'OR'
    SOME = r'SOME'


    EQUAL = r'\='

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
    @_(r'[A-Za-z][A-Za-z0-9_]*')
    def NAME(self,t):
        return t


    @_('TRUE')
    def BOOL(self,t):
        t.value=1
        return t

    @_('FALSE')
    def BOOL(self,t):
        t.value=0
        return t

    @_('UNKNOWN')
    def BOOL(self,t):
        t.value=-1
        return t

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