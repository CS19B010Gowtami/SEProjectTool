from sly import Parser
from basic_sly_lexer import MyLexer
class MyParser(Parser):
    tokens = MyLexer.tokens

    @_("stmt SEMICOLON")
    def stmt_list(self,p):
        return
    
    @_("stmt_list stmt SEMICOLON")
    def stmt_list(self,p):
        return

    @_("NAME")
    def expr(self,p):
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
