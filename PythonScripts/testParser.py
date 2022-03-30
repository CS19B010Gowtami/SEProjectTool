from sly import Parser
from lexer import MyLexer

x=[]

class MyParser(Parser):
    tokens = MyLexer.tokens

    # Grammar rules and actions
    # @_('SELECT IDENTIFIER FROM IDENTIFIER SEMICOLON')
    # def select(self, p):
    #     return p.expr + p.term

    start = 's'
    # start - query_list

    @_('INSERT')
    def s(self,p):
        return
    @_('INTO')
    def s(self,p):
        return
    @_('TABLE INSERT IDENTIFIER')
    def s(self,p):
        print("Working??")
        return p[2]


    @_('LCB val_list RCB')
    def s(self,p):
        return

    @_('val_list COMMA INTNUM')
    def val_list(self,p):
        x.append(p[2])
        return

    
    @_('INTNUM')
    def val_list(self,p):
        x.append(p[0])
        return p[0]

if __name__ == '__main__':
    lexer = MyLexer()
    parser = MyParser()

    # while True:
    try:
        # text = input(' Input > ')
        tokenTester = '''
        (10,20,30,40,50)'''
        result = parser.parse(lexer.tokenize(tokenTester))
        print(result)
        print(x)
    except EOFError:
        print("EOF")
