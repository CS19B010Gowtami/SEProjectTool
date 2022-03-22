from sly import Parser
from basic_sly_lexer import MyLexer
class MyParser(Parser):
    tokens = MyLexer.tokens

# Grammar rules and actions
    # @_('SELECT names FROM names SEMICOLON')
    # def select(self, p):
    #     return p.expr + p.term
    @_('SELECT items FROM item ')
    def select(self, p):
        return
    @_('NAMES')
    def item(self, p):
        return p.NAMES
    @_('items COMMA item')
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
