from sly import Parser
from lexer import MyLexer


class MyParser(Parser):
    tokens = MyLexer.tokens

    # Grammar rules and actions
    # @_('SELECT ID FROM ID SEMICOLON')
    # def select(self, p):
    #     return p.expr + p.term

    @_('query_list')
    def start(self,p):
    	return

    @_('query query_list')
    def query_list(self,p):
        return

    @_('select_stmt')
    def query(self,p):
        return

    @_('update_stmt')
    def query(self,p):
        return

    @_('insert_stmt')
    def query(self,p):
        return


    @_('delete_stmt')
    def query(self,p):
        return

    @_('')
    def empty(self, p):
        pass

    @_('empty')
    def query(self,p):
        return

    @_('SELECT is_distinct col_list FROM table_list opt_where_cond  SEMICOLON')
    def select_stmt(self, p):
        return

    # @_('SELECT is_distinct col_list FROM table_list nest_cond opt_where_cond  SEMICOLON')
    # def select_stmt(self, p):
    #     return

    # Grammar for nested queries part of release 2
    # @_('SELECT is_distinct col_list FROM ( select_stmt )')
    # def select_stmt(self,p):
    #     return

    @('DISTINCT','empty')
    def is_distinct(self,p):
        return

    @_('empty')
    def opt_where_clause(self,p):
        return

    @_('ID COMMA ID', 'ID','*')
    def col_list(self,p):
        return

    @_('ID COMMA ID','ID')
    def tab_list(self, p):
        return

    @_('WHERE conds','empty')
    def opt_where_cond(self,p):
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

    @_('conds OR cond','conds AND cond','NOT cond','cond')
    def conds(self, p):
        return 
        
    # @_('conds AND cond')
    # def conds(self, p):
    #     return
    # @_('NOT cond')
    # def conds(self, p):
    #     return 
    # @_('cond')
    # def conds(self, p):
    #     return

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
