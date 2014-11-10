# This is the javascript lexer.
# Called from the html lexer.
# It further tokenizes the javascript token received from the html lexer.
#

import ply.lex as lex

class JavascriptLexer:

    # List of javascirpt tokens
    tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
        'IDENTIFIER',   # factorial
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'MOD',          # %
        'NOT',          # !
        'NUMBER',       # 1234 5.678
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'STRING',       # "this is a \"tricky\" string"
        'TIMES',        # *
        'TRUE',         # TRUE
        'VAR',          # var
        'WHILE',        # while
    )

    states = (
        ('comments', 'exclusive'),    # /* ..... */
    )

    def t_comments(self, t):
        r'/\*'
        t.lexer.begin('comments')
        pass

    def t_comments_end(self, t):
        r'\*/'
        t.lexer.lineno += t.value.count('\n')
        t.lexer.begin('INITIAL')
        pass

    def t_comments_error(self, t):
        t.lexer.skip(1)

    t_comments_ignore = ' \t\v\r' # Although ignore tules

    def t_eol_comments(self, t):
        r'//.*'
        pass
        # Note that . matches everything other than the new line character. So
        # Everything in that line upto the newline character will be treated as
        # comments and passed. The newline character afterwards will be caught
        # by the special rule, t_newline.

    # Token definitions for the INTIAL state:

    reserved = ('if', 'then', 'else', 'true', 'false', 'function', 'var', 'return', 'while',)
    # the reserved words are also identifiers, therefore find all the identifier and check if they are reserved words.
    # escape the characters that have meaning in the regular expressions like +, ?, |, etc.

    t_ANDAND        = r'&&'
    t_COMMA         = r','
    t_DIVIDE        = r'/'
    t_EQUALEQUAL    = r'=='
    t_EQUAL         = r'='
    t_LPAREN        = r'\('
    t_LBRACE        = r'{'
    t_RBRACE        = r'}'
    t_SEMICOLON     = r';'
    t_MINUS         = r'-'
    t_MOD           = r'%'
    t_NOT           = r'!'
    t_OROR          = r'\|\|'
    t_PLUS          = r'\+'
    t_RPAREN        = r'\)'
    t_TIMES         = r'\*'
    t_LE            = r'<='
    t_LT            = r'<'
    t_GT            = r'>'
    t_GE            = r'>='

    def t_IDENTIFIER(self, t):
        r'[a-zA-Z][a-zA-Z_]*'
        if t.value in self.reserved:
            t.type = t.value.upper()
        return t

    def t_NUMBER(self, t):
        r'-?[0-9]+(?:\.[0-9]*)?'
        t.value = float(t.value)
        return t

    def t_STRING(self, t):
        r'"(?:[^"\\]|(?:\\.))*"'
        t.value = t.value[1:-1]
        return t
    # How the string works:
    # First character should be a double quote
    # Last character should be a double quote
    # In the middle we can have 0 or more characters
    # The middle characters can either be anything other than double quotes and slash or -> ABC DEF?
    # or they can be slash followed by any single character character. -> \" \"
    # Example:
    # "ABC \" DEF?\""

    def t_newline(self, t):
        r'\n'
        t.lexer.lineno += 1
        pass

    t_ignore = ' \t\v\r'

    def t_error(self, t):
        print "Illegal character encountered by javascript lexer ", t.value[0]
        t.lexer.skip(1)

    # Building the javascript lexer:
    def build(self):
        self.jslex = lex.lex(module=self)

    # Input into the javascript lexer:
    def sendInput(self, input_data):
        self.jslex.input(input_data)

    # Output the result:
    def showOutput(self):
        result = []
        while True:
            tok = self.jslex.token()
            if not tok:
                break
            result = result + [tok.type]
        return result

# Testing the class
# input = """"""
# my = JavascriptLexer()
# my.build()
# my.sendInput(input) # Easier if the input is a triple quoted string instead of a single quoted. This may prevent problems appearing with strings type tokens.
# my.showOutput()
