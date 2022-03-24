from sly import Parser
from basic_sly_lexer import MyLexer
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


    @_('empty')
    def query(self,p):
        return
    @_('SELECT is_distinct col_list FROM table_list or nest opt_where_clause SEMICOLON')
    def select_stmt(self, p):
        return

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

    @_('WHERE conds')
    def opt_where_clause(self,p):
        return

    # @_('SELECT col_list FROM item WHERE conds SEMICOLON')
    # def select_stmt(self, p):
    #     return

    @_('conds OR cond')
    def conds(self, p):
        return 
    @_('conds AND cond')
    def conds(self, p):
        return
    @_('NOT cond')
    def conds(self, p):
        return 
    @_('cond')
    def conds(self, p):
        return

    @_('cond')
    def cond(self, p):
        return p.cond
    
    @_('ID EQUAL NUMS')
    def cond(self, p):
        return p.ID == p.NUMS
    @_('ID GTEQ NUMS')
    def cond(self, p):
        return p.ID >= p.NUMS
    @_('ID LTEQ NUMS')
    def cond(self, p):
        return p.ID <= p.NUMS
    @_('ID GTOP NUMS')
    def cond(self, p):
        return p.ID > p.NUMS
    @_('ID LTOP NUMS')
    def cond(self, p):
        return p.ID < p.NUMS
    @_('ID NOTEQ NUMS')
    def cond(self, p):
        return p.ID != p.NUMS


    @_('*')
    def col_list(self,p):
        return

    @_('col_item COMMA col_list')
    def col_list(self,p):
        return

    @_('ID')
    def item(self, p):
        return p.ID

    @_('items COMMA item')
    def items(self, p):
        return p.items , p.item

    @_('DISTINCT items COMMA item')
    def items(self, p):
        return 

    @_('item')
    def items(self, p):
       return p.item

    @_('')
    def empty(self, p):
        pass
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
