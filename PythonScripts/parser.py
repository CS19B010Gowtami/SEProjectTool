import re
from numpy import sort
from sly import Parser
from lexer import MyLexer

class Query():
    # Specs = {}
    # ColumnList = []
    # ValueList = []
    def __init__(self):
        self.Specs = {}
        self.ColumnList = []
        self.ValueList = []

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
        if(column_name in self.ColumnList):
            return
        self.ColumnList.append(column_name)

    def addToValueList(self, value):
        self.ValueList.append(value)

    def createQueryParameter(self):
        return

    def projectParameter(self):
        return
Q = Query()
class MyParser(Parser):
    tokens = MyLexer.tokens

    precedence = (
       ('left', "OR"),
       ('left', "AND"),
       ('left', "NOT"),
    )

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
        # print("Id Printed", p[2])
        return

    @_('IDENTIFIER')
    def insert_col_list(self, p):
        Q.addToColumnList(p[0])
        # print("One Id Printed", p[0])
        return

    @_('val_list COMMA value')
    def val_list(self, p):
        Q.addToValueList(p[2])
        return

    @_('value')
    def val_list(self, p):
        Q.addToValueList(p[0])
        return
    # --------------- INSERT STATEMENT ---------------


    # --------------- SELECT STATEMENT ---------------
    @_('SELECT is_distinct select_param FROM IDENTIFIER select_opt_where sort_order opt_limit')
    def select_stmt(self, p):
        Q.Specs["table_name"]=p[4]
        Q.Specs["select_cond_tree"]=p[5]
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
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"]=0
        return

    @_('MULOP')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"]=0
        return

    @_('MAX LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"]=1
        Q.Specs["aggr"]="MAX"
        Q.Specs["aggr_list"]= p[2]
        return

    @_('MIN LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"]=1
        Q.Specs["aggr"]="MIN"
        Q.Specs["aggr_list"]= p[2]
        return

    @_('COUNT LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"]=1
        Q.Specs["aggr"]="COUNT"
        Q.Specs["aggr_list"]= p[2]
        return

    @_('COUNT LCB MULOP RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"]=1
        Q.Specs["aggr"]="COUNT"
        Q.Specs["aggr_list"]= p[2]
        return

    @_('SUM LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"]=1
        Q.Specs["aggr"]="SUM"
        Q.Specs["aggr_list"]= p[2]
        return

    @_('AVG LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"]=1
        Q.Specs["aggr"]="AVG"
        Q.Specs["aggr_list"] = p[2]
        return

    @_('select_col_list COMMA IDENTIFIER opt_aliasing')
    def select_col_list(self, p):
        Q.addToColumnList(p[2])
        if(p[3]!=''):
            Q.Specs['alias_map'][p[2]] = p[3]
        return

    @_('IDENTIFIER opt_aliasing')
    def select_col_list(self, p):
        Q.addToColumnList(p[0])
        Q.Specs['alias_map'] = {}
        if(p[1]!=''):
            Q.Specs['alias_map'][p[0]] = p[1]
        return

    @_('AS IDENTIFIER')
    def opt_aliasing(self,p):
        return p[1]

    @_('')
    def opt_aliasing(self,p):
        return ''

    @_('WHERE condition_list')
    def select_opt_where(self,p):
        return p[1]

    @_('WHERE IDENTIFIER IS NULL')
    def select_opt_where(self, p):
        return

    @_('WHERE IDENTIFIER IS NOT NULL')
    def select_opt_where(self, p):
        return 

    @_('')
    def select_opt_where(self,p):
        return ''

    @_('NOT condition_list')
    def condition_list(self, p):
        return ('NOT',p[1])

    @_('condition_list AND condition_list')
    def condition_list(self, p):
        return ('AND',p[0],p[2])

    @_('condition_list OR condition_list')
    def condition_list(self, p):
        return ('OR',p[0],p[2])


    @_('condition')
    def condition_list(self, p):
        return p[0]

    @_('IDENTIFIER EQUAL value','IDENTIFIER GTEQ value','IDENTIFIER LTEQ value','IDENTIFIER GTOP value','IDENTIFIER LTOP value','IDENTIFIER NOTEQ value')
    def condition(self, p):
        # print(p[0],p[1],p[2])
        return (p[0],p[1],p[2])

    @_('LCB condition_list RCB')
    def condition(self,p):
        return (p[1])

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
        Q.Specs["table_name"]=p[2]
        # Either Empty or a tree of tuple as a node
        Q.Specs["delete_cond_tree"]=p[3]
        return
    
    @_('WHERE condition_list')
    def delete_opt_where(self,p):
        return p[1]

    @_('')
    def delete_opt_where(self,p):
        return ""
    # --------------- DELETE STATEMENT ---------------
    
    
    # --------------- UPDATE STATEMENT ---------------
    
    @_('UPDATE IDENTIFIER SET col_assigns select_opt_where')
    def update_stmt(self, p):
        Q.Specs["table_name"]=p[1]
        # Either Empty or a tree of tuple as a node
        Q.Specs["update_cond_tree"]=p[4]
        return 
    
    @_('col_assigns COMMA col_assign')
    def col_assigns(self, p):
        return
    
    @_('col_assign')
    def col_assigns(self, p):
        return
    
    @_('column_name EQUAL value')
    def col_assign(self, p):
        # adding column = value for update parameter
        Q.addToColumnList(p[0])
        Q.addToValueList(p[2])
        return
    
    @_('IDENTIFIER')
    def column_name(self, p):
        return p[0]

    @_('INTNUM','REALNUM','STRING')
    def value(self, p):
        # Q.addToValueList(p[0])
        # print("One val Printed", p[0])
        # print(p[0].type)
        # try:
        #     print(p.STRING)
        #     print("Issue with String")
        # except ValueError:
        #     print("PROBLEM")
        return p[0]
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
        selectText = '''SELECT abc,cde AS kek FROM TAasasfBLE WHERE KEK > 10 OR top > 50 AND somee =10 ;'''
        deleteText = '''DELETE FROM TAEEE;'''
        tokenTester = '''
        INSERT INTO GG (col1,col2,col3,col4,col4) VALUES (10,20,30,40,50);'''
        updateTester = '''
        UPDATE Customers
        SET ContactName='Juan' WHERE Country='Mexico';'''
        result = parser.parse(lexer.tokenize(selectText))
        print(result)
    except EOFError:
        print("EOF Error")

