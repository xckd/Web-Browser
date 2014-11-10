import JSLexer

mylexer = JSLexer.JavascriptLexer()
mylexer.build()

def test_lexer(input_string):
    mylexer.sendInput(input_string)
    # result = [ ]
    # while True:
    #     tok = mylexer.jslex.token()
    #     if not tok: break
    #     print tok
    #     result = result + [tok.type]
    #     return result
    return mylexer.showOutput()

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print test_lexer(input1) == output1

input2 = """
if // else mystery
=/*=*/=
true /* false
*/ return"""

output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']

print test_lexer(input2) == output2
