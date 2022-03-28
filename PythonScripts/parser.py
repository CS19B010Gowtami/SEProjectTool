from sly import Parser
from lexer import MyLexer


class MyParser(Parser):
    tokens = MyLexer.tokens

    # Grammar rules and actions
    # @_('SELECT ID FROM ID SEMICOLON')
    # def select(self, p):
    #     return p.expr + p.term


    # start - query_list
    @_('query_list')
    def start(self,p):
        return

    # query_list - query query_list
    @_('query query_list')
    def query_list(self,p):
        return

    @_('select_stmt SEMICOLON')
    def query(self,p):
        return

    @_('update_stmt SEMICOLON')
    def query(self,p):
        return

    @_('insert_stmt SEMICOLON')
    def query(self,p):
        return

    @_('delete_stmt SEMICOLON')
    def query(self,p):
        return
    
    # --------------- INSERT STATEMENT ---------------
    @_('INSERT INTO IDENTIFIER LCB insert_col_list RCB VALUES LCB val_list RCB')
    def insert_stmt(self, p):
        return

    @_('insert_col_list COMMA IDENTIFIER')
    def insert_col_list(self, p):
        return
    
    @_('IDENTIFIER')
    def insert_col_list(self, p):
        return

    @_('val_list COMMA val')
    def val_list(self, p):
        return
    
    @_('val')
    def val_list(self, p):
        return
    # --------------- INSERT STATEMENT ---------------

    # --------------- SELECT STATEMENT ---------------
    @_('SELECT is_distinct select_param FROM IDENTIFIER select_opt_where sort_order opt_limit')
    def select_stmt(self, p):
        return 

    @_('DISTINCT')
    def is_distinct(self, p):
        return 1

    @_('')
    def is_distinct(self, p):
        return 0

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
        return
    
    @_('IDENTIFIER opt_aliasing')
    def select_col_list(self, p):
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
        return 0

    @_('ORDER BY DESC')
    def sort_order(self, p):
        return 1

    @_('')
    def sort_order(self, p):
        return 0

    @_('LIMIT INTNUM OFFSET INTMUM')
    def opt_limit(self, p):
        return

    @_('LIMIT INTNUM')
    def opt_limit(self, p):
        return

    @_('')
    def opt_limit(self, p):
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

    # Incomplete ig
    # --------------- DELETE STATEMENT ---------------


    # @_('SELECT is_distinct col_list FROM table_list opt_where_cond SEMICOLON')
    # def select_stmt(self, p):
    #     return

    # @_('SELECT is_distinct col_list FROM table_list nest_cond opt_where_cond  SEMICOLON')
    # def select_stmt(self, p):
    #     return

    # Grammar for nested queries part of release 2
    # @_('SELECT is_distinct col_list FROM ( select_stmt )')
    # def select_stmt(self,p):
    #     return

    @_('ID COMMA ID', 'ID','*')
    def col_list(self,p):
        return

    @_('ID COMMA ID','ID')
    def tab_list(self, p):
        return
  
#   NESTED CONDITION
    # @_('nest','empty')
    # def nest_cond(self, p):
    #     return
    
    # @_('WHERE IN select_stmt','WHERE NOT IN select_stmt','WHERE ANY select_stmt','WHERE ALL select_stmt')
    # def nest(self, p):
    #     return

    # @_('SELECT col_list FROM item WHERE conds SEMICOLON')
    # def select_stmt(self, p):
    #     return

    # @_('conds OR cond','conds AND cond','NOT cond','cond')
    # def conds(self, p):
    #     return 

    # @_('cond')
    # def conds(self, p):
    #     return p.cond
    # @_('cond')
    # def cond(self, p):
    #     return p.cond
    
    @_('ID EQUAL NUMS','ID GTEQ NUMS','ID LTEQ NUMS','ID GTOP NUMS','ID LTOP NUMS','ID NOTEQ NUMS')
    def cond(self, p):
        return (p[1], p.ID, p.NUMS)

    # @_('ID GTEQ NUMS')
    # def cond(self, p):
    #     return p.ID >= p.NUMS
    # @_('ID LTEQ NUMS')
    # def cond(self, p):
    #     return p.ID <= p.NUMS
    # @_('ID GTOP NUMS')
    # def cond(self, p):
    #     return p.ID > p.NUMS
    # @_('ID LTOP NUMS')
    # def cond(self, p):
    #     return p.ID < p.NUMS
    # @_('ID NOTEQ NUMS')
    # def cond(self, p):
    #     return p.ID != p.NUMS

    @_('ID')
    def item(self, p):
        return p.ID

    @_('')
    def empty(self, p):
        pass

    @_('empty')
    def query(self,p):
        return


if __name__ == '__main__':
    lexer = MyLexer()
    parser = MyParser()

    while True:
        try:
            text = input(' Input > ')
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break
