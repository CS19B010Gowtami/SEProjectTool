import ply.yacc as yacc
import mylexer               # Import lexer information
tokens = mylexer.tokens      # Need token list

def p_select(p):{
' ' 'select : SELECT STRING FROM STRING SEMICOLON' ' '
}
def p_where(p):{
    ' ' 'where : SELECT STRING FROM STRING WHERE condition SEMICOLON' ' '
}
def p_condition(p):{
    ' ' 'condition : STRING EQUAL nums 
                     |
                     STRING EQUAL STRING 
                     |
                     STRING relation nums 
                     |
                     STRING BETWEEN nums AND nums' ' '
}
def p_relation(p): {
    ' ' 'relation : EQUAL 
                    | GTOP |  LTOP | GTEQ | LTEQ | NOTEQ' ' '
}
def p_nums(p):{
    ' ' 'nums : REALNUM | INTNUM' ' '
}
yacc.yacc() 