from sly import Lexer

class MyLexer(Lexer):

    # these are set of tokens that are to be exported to the parser
    tokens = {
        SUM,
        COUNT,
        AVG,
        MIN,
        MAX,
        REALNUM,
        INTNUM,
        COL_NAME,
        TABLE_NAME,
        STRING,
        CHARACTER,
        IDENTIFIER,
        EQUAL,
        ADDEQ,
        SUBEQ,
        MULEQ,
        DIVEQ,
        MODEQ,
        GTEQ,
        LTEQ,
        NOTEQ,
        ANDEQ,
        OREQ,
        XOREQ,
        ADDOP,
        SUBOP,
        MULOP,
        DIVOP,
        MODOP,
        GTOP,
        LTOP,
        ANDOP,
        OROP,
        XOROP,
        SEPARATORS,
        SEMICOLON,
        COMMA,
        LCB,
        RCB,
        LFB,
        RFB,
        LSB,
        NAMES,
        NUMS,
        RELOP,
        RSB,
        UPDATE,
        BACKUP,
        FROM,
        DISTINCT,
        LIMIT,
        ORDER,
        ADD,
        DATABASE,
        BETWEEN,
        ASC,
        CASE,
        EXISTS,
        AND,
        TRUNCATE,
        PROCEDURE,
        WHERE,
        VALUES,
        ALL,
        HAVING,
        LIKE,
        EXEC,
        CONSTRAINT,
        COLUMN,
        DEFAULT,
        ROWNUM,
        REPLACE,
        IS,
        SET,
        LEFT,
        AS,
        FULL,
        ALTER,
        RIGHT,
        GROUP,
        INTO,
        SHOW,
        ANY,
        NULL,
        BY,
        INSERT,
        SELECT,
        NOT,
        TABLE,
        KEY,
        USE,
        TOP,
        UNION,
        INNER,
        CHECK,
        JOIN,
        FOREIGN,
        PRIMARY,
        IN,
        UNIQUE,
        VIEW,
        DELETE,
        OUTER,
        VARCHAR,
        OR,
        INDEX,
        DROP,
        CREATE,
        SOME,
        DESC,
        BOOL,
        DOT,
        OFFSET
	}

    # Identifiers and keywords
    IDENTIFIER = r'[a-zA-Z_\.][a-zA-Z0-9_\.]*'

    IDENTIFIER['ADD'] = ADD
    IDENTIFIER['CONSTRAINT'] = CONSTRAINT
    IDENTIFIER['ALTER'] = ALTER
    IDENTIFIER['COLUMN'] = COLUMN
    IDENTIFIER['TABLE'] = TABLE
    IDENTIFIER['AS'] = AS
    IDENTIFIER['ASC'] = ASC
    IDENTIFIER['BACKUP'] = BACKUP
    IDENTIFIER['DATABASE'] = DATABASE
    IDENTIFIER['CASE'] = CASE
    IDENTIFIER['CHECK'] = CHECK
    IDENTIFIER['CREATE'] = CREATE
    IDENTIFIER['INDEX'] = INDEX
    IDENTIFIER['REPLACE'] = REPLACE
    IDENTIFIER['VIEW'] = VIEW
    IDENTIFIER['PROCEDURE'] = PROCEDURE
    IDENTIFIER['UNIQUE'] = UNIQUE
    IDENTIFIER['DEFAULT'] = DEFAULT
    IDENTIFIER['DELETE'] = DELETE
    IDENTIFIER['DESC'] = DESC
    IDENTIFIER['DISTINCT'] = DISTINCT
    IDENTIFIER['DROP'] = DROP
    IDENTIFIER['USE'] = USE
    IDENTIFIER['SHOW'] = SHOW
    IDENTIFIER['EXEC'] = EXEC
    IDENTIFIER['FOREIGN'] = FOREIGN
    IDENTIFIER['KEY'] = KEY
    IDENTIFIER['FROM'] = FROM
    IDENTIFIER['FULL'] = FULL
    IDENTIFIER['OUTER'] = OUTER
    IDENTIFIER['JOIN'] = JOIN
    IDENTIFIER['GROUP'] = GROUP
    IDENTIFIER['BY'] = BY
    IDENTIFIER['HAVING'] = HAVING
    IDENTIFIER['INNER'] = INNER
    IDENTIFIER['INSERT'] = INSERT
    IDENTIFIER['INTO'] = INTO
    IDENTIFIER['SELECT'] = SELECT
    IDENTIFIER['NULL'] = NULL
    IDENTIFIER['IS'] = IS
    IDENTIFIER['LEFT'] = LEFT
    IDENTIFIER['LIMIT'] = LIMIT
    IDENTIFIER['ORDER'] = ORDER
    IDENTIFIER['PRIMARY'] = PRIMARY
    IDENTIFIER['RIGHT'] = RIGHT
    IDENTIFIER['ROWNUM'] = ROWNUM
    IDENTIFIER['TOP'] = TOP
    IDENTIFIER['SET'] = SET
    IDENTIFIER['TRUNCATE'] = TRUNCATE
    IDENTIFIER['UNION'] = UNION
    IDENTIFIER['UPDATE'] = UPDATE
    IDENTIFIER['VALUES'] = VALUES
    IDENTIFIER['WHERE'] = WHERE
    IDENTIFIER['VARCHAR'] = VARCHAR
    IDENTIFIER['ALL'] = ALL
    IDENTIFIER['AND'] = AND
    IDENTIFIER['ANY'] = ANY
    IDENTIFIER['BETWEEN'] = BETWEEN
    IDENTIFIER['EXISTS'] = EXISTS
    IDENTIFIER['IN'] = IN
    IDENTIFIER['LIKE'] = LIKE
    IDENTIFIER['NOT'] = NOT
    IDENTIFIER['OR'] = OR
    IDENTIFIER['SOME'] = SOME
    IDENTIFIER['OFFSET'] = OFFSET
    # EXTRAS 
    IDENTIFIER['SUM'] = SUM
    IDENTIFIER['COUNT'] = COUNT
    IDENTIFIER['MIN'] = MIN
    IDENTIFIER['MAX'] = MAX
    IDENTIFIER['AVG'] = AVG

    EQUAL = r'\='
    COMMA = r'\,'
    DOT   = r'\.'

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
    XOREQ = r'\^\='

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
    XOROP = r'\^'

    SEPARATORS = r'\,'
    SEMICOLON = r'\;'
    LCB = r'\('
    RCB = r'\)'
    LFB = r'\{'
    RFB = r'\}'
    LSB = r'\['
    RSB = r'\]'


    INTNUM = r'\d+'
    REALNUM = r'\d+.\d+'
    # Should String Have New Line OR NOT..? Problematic
    # \'.*\' matches longest so in between thing cannot be \' .......That's all
    STRING = r'\'([ \t\n\r\f\v]|[^ \'\t\n\r\f\v])+\''
    # STRING = r'\'.*\''
    # @_(r'''("[^"\\]*(\\.[^"\\]*)*"|'[^'\\]*(\\.[^'\\]*)*')''')

    ignore = r'\t '
    
    def IDENTIFIER(self,t):
        return t
    
    @_('TRUE')
    def BOOL(self,t):
        t.value=1
        return t

    @_('FALSE')
    def BOOL(self,t):
        t.value=0
        return t


    # @_('UNKNOWN')
    # def BOOL(self,t):
    #     t.value=-
    #     return t

    def INTNUM(self, t):
        t.value = int(t.value)
        return t

    def REALNUM(self, t):
        t.value = float(t.value)
        return t

    
    # @_(r'''('\d+'|'\\d+.\d+')''')
    # def NUMS(self, t):
    #     return t

    def STRING(self, t):
        l = len(t.value)
        t.value = t.value[1:(l-1)]
        try:
            t.value = int(t.value)
            t.type = 'INTNUM'
        except ValueError:
            try:
                t.value = float(t.value)
                t.type = 'REALNUM'
            except ValueError:
                t.type = 'STRING'	
        return t

    # ignore_comment = r'\#.*'
    @_(r'#.*')
    def COMMENT(self, t):
        pass

	# Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print('Line %d: Bad Character -> %r' % (self.lineno, t.value[0]))
        self.index += 1

if __name__ == '__main__':
	data = tokenTester = '''
        (10,20,30,40,50)'''
	lexer = MyLexer()
	for tok in lexer.tokenize(tokenTester):
		print(tok)
