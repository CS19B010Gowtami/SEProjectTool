from sly import Parser
from lexer import MyLexer

class Query():
    Specs = {}
    ColumnList = []
    ValueList = []

    # def convertCode()
    def debugStructure(self):
        print(self.Specs)
        print(self.ValueList)
        print(self.ColumnList)

    def clearStructure(self):
        self.Specs.clear()
        self.ColumnList.clear()
        self.ValueList.clear()

    def addToColumnList(self, column_name):
        # check for duplicates
        self.ColumnList.append(column_name)

    def addToValueList(self, value):
        self.ValueList.append(value)


Q = Query()
class MyParser(Parser):
    tokens = MyLexer.tokens

    start = 'start1'
    # start - query_list
    @_('query_list')
    def start1(self,p):
        return p[0]

    # query_list - query query_list
    @_('query query_list')
    def query_list(self,p):
        # Q.convertCode()
        Q.debugStructure()
        Q.clearStructure()
        return p[0]

    @_('empty')
    def query_list(self,p):
        return

    @_('')
    def empty(self,p):
        pass

    @_('select_stmt SEMICOLON')
    def query(self,p):
        Q.Specs["type"]="select"
        return "SELECT_STATEMENT"

    @_('update_stmt SEMICOLON')
    def query(self,p):
        Q.Specs["type"]="update"
        return "UPDATE_STATEMENT"

    @_('insert_stmt SEMICOLON')
    def query(self,p):
        Q.Specs["type"]="insert"
        return "INSERT_STATEMENT"

    @_('delete_stmt SEMICOLON')
    def query(self,p):
        Q.Specs["type"]="delete"
        return "DELETE_STATEMENT"

    # --------------- INSERT STATEMENT ---------------
    @_('INSERT INTO IDENTIFIER LCB insert_col_list RCB VALUES LCB val_list RCB')
    def insert_stmt(self, p):
        Q.Specs["table_name"]=p[2]
        return
    
    @_('insert_col_list COMMA IDENTIFIER')
    def insert_col_list(self, p):
        Q.addToColumnList(p[2])
        print("Id Printed", p[2])
        return

    @_('IDENTIFIER')
    def insert_col_list(self, p):
        Q.addToColumnList(p[0])
        print("One Id Printed", p[0])
        return

    @_('val_list COMMA value')
    def val_list(self, p):
        return

    @_('value')
    def val_list(self, p):
        return
    # --------------- INSERT STATEMENT ---------------


    # --------------- SELECT STATEMENT ---------------
    @_('SELECT is_distinct select_param FROM IDENTIFIER select_opt_where sort_order opt_limit')
    def select_stmt(self, p):
        Q.Specs["table_name"]=p[4]
        return 

    @_('DISTINCT')
    def is_distinct(self, p):
        Q.Specs["is_distinct"]=1
        return

    @_('')
    def is_distinct(self, p):
        Q.Specs["is_distinct"]=0
        return

    @_('select_col_list')
    def select_param(self, p):
        return

    @_('MULOP')
    def select_param(self, p):
        return

    @_('MAX LCB IDENTIFIER RCB')
    def select_param(self, p):
        return

    @_('MIN LCB IDENTIFIER RCB')
    def select_param(self, p):
        return

    @_('COUNT LCB IDENTIFIER RCB')
    def select_param(self, p):
        return

    @_('COUNT LCB MULOP RCB')
    def select_param(self, p):
        return

    @_('SUM LCB IDENTIFIER RCB')
    def select_param(self, p):
        return

    @_('AVG LCB IDENTIFIER RCB')
    def select_param(self, p):
        return

    @_('select_col_list COMMA IDENTIFIER opt_aliasing')
    def select_col_list(self, p):
        Q.addToColumnList(p[2])
        return

    @_('IDENTIFIER opt_aliasing')
    def select_col_list(self, p):
        Q.addToColumnList(p[0])
        return

    @_('AS IDENTIFIER')
    def opt_aliasing(self,p):
        return

    @_('WHERE condition_list')
    def select_opt_where(self,p):
        return

    @_('WHERE IDENTIFIER IS NULL')
    def select_opt_where(self, p):
        return

    @_('WHERE IDENTIFIER IS NOT NULL')
    def select_opt_where(self, p):
        return

    @_('')
    def select_opt_where(self,p):
        return

    @_('NOT condition_list')
    def condition_list(self, p):
        return

    @_('condition ANDOP condition_list')
    def condition_list(self, p):
        return

    @_('condition OROP condition_list')
    def condition_list(self, p):
        return

    @_('condition')
    def condition_list(self, p):
        return

    @_('ORDER BY ASC')
    def sort_order(self, p):
        Q.Specs["sort_order"]=0
        return

    @_('ORDER BY DESC')
    def sort_order(self, p):
        Q.Specs["sort_order"]=1
        return

    @_('')
    def sort_order(self, p):
        Q.Specs["sort_order"]=0
        return

    @_('LIMIT INTNUM opt_offset')
    def opt_limit(self, p):
        Q.Specs["limit_value"]=p[1]
        return

    @_('')
    def opt_limit(self, p):
        return

    @_('OFFSET INTNUM')
    def opt_offset(self, p):
        Q.Specs["offset"]=p[1]
        return

    @_('')
    def opt_offset(self, p):
        return
    # --------------- SELECT STATEMENT ---------------


    # --------------- DELETE STATEMENT ---------------
    @_('DELETE FROM IDENTIFIER delete_opt_where')
    def delete_stmt(self, p):
        return
    
    @_('WHERE condition_list')
    def delete_opt_where(self,p):
        return 

    @_('')
    def delete_opt_where(self,p):
        return
    # --------------- DELETE STATEMENT ---------------
    
    
    # --------------- UPDATE STATEMENT ---------------
    @_('IDENTIFIER EQUAL NUMS','IDENTIFIER GTEQ NUMS','IDENTIFIER LTEQ NUMS','IDENTIFIER GTOP NUMS','IDENTIFIER LTOP NUMS','IDENTIFIER NOTEQ NUMS')
    def condition(self, p):
        return

    @_('UPDATE IDENTIFIER SET col_assigns select_opt_where')
    def update_stmt(self, p):
        return 
    
    @_('col_assigns COMMA col_assign')
    def col_assigns(self, p):
        return
    
    @_('col_assign')
    def col_assigns(self, p):
        return
    
    @_('column_name EQUAL value')
    def col_assign(self, p):
        return
    
    @_('IDENTIFIER')
    def column_name(self, p):
        return

    @_('INTNUM','REALNUM','STRING')
    def value(self, p):
        Q.addToValueList(p[0])
        
        print("One val Printed", p[0])
        return 
    # --------------- UPDATE STATEMENT ---------------

    def error(self, p):
        if p:
            print("Syntax error at token", p.type, p.value)
            # Just discard the token and tell the parser it's okay.
            # self.errok()
        else:
            print("Syntax error at EOF")


if __name__ == '__main__':
    lexer = MyLexer()
    parser = MyParser()

    # while True:
    try:
        # text = input(' Input > ')
        selectText = '''SELECT * FROM TAasasfBLE;'''
        deleteText = '''DELETE FROM TAEEE;'''
        tokenTester = '''
        INSERT INTO GG (col1,col2,col3,col4) VALUES (10,20,30,40,50);'''
        result = parser.parse(lexer.tokenize(tokenTester))
        print(result)
    except EOFError:
        print("EOF Error")
