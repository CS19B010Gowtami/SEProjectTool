from sly import Parser
from basic_sly_lexer import MyLexer
class MyParser(Parser):
    tokens = MyLexer.tokens

# Grammar rules and actions
    # @_('SELECT ID FROM ID SEMICOLON')
    # def select(self, p):
    #     return p.expr + p.term
    @_('SELECT items FROM item SEMICOLON')
    def select(self, p):
        return
    @_('SELECT items FROM item WHERE conds SEMICOLON')
    def select(self, p):
        return 
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
        return p.cond
     @_('cond')
    def cond(self, p):
        return p.cond
    
    @_('ID EQUAL NUMS')
    def cond(self, p):
        return p.ID = p.NUMS
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
        return p.ID <> p.NUMS   

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
