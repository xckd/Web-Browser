# This is the lexer to create tokenize the webpage html
# and also separate the javascript elements.
#

import ply.lex as lex

class HtmlLexer:

    # List of tokens:
    tokens = (
        'LANGLE',       # <
        'LANGLESLASH',  # </
        'RANGLE',       # >
        'STRING',       # something within single quotes or double quotes. <a href="www.google.com"> text to appear </a> Also drop the quotes before returning.
                        # 'This is the "value" of the webpage.' -> value will have string type and others will have word type.
        'WORD',         # a word without = , < > , no white spaces. bold, tags, etc. a, href, etc. Put the word definition below string so that quotes strings do not get counted as words.
        'EQUAL',        # =
        'JAVASCRIPT'    # within script tags.
    )

    # List of states:
    states = (
        ('htmlcomment','exclusive'),   # <!-- html code -->
        ('javascript','exclusive'),    # <script type="text/javascript">
    )

    # Token definitions for the htmlcomments state:
    def t_htmlcomment(self, t): # This name could be anything. This is actually an INITIAL token definition. But it should be put at the beginning so that it is considered first and then the control goes to the htmlcomment states immediately without going into the INITIAL state.
      r'<!--'
      t.lexer.begin('htmlcomment')

    t_htmlcomment_ignore = ' \t\v\r'

    def t_htmlcomment_error(self, t):
      t.lexer.skip(1) # for every character this is the rule that gets executed as there is no other rules.
      # Now .skip function causes gathering up of the current element to the t.value without destroying the previous value.
      # It just appends the new character to the previous one. So that when htmlcomment_end is encountered, t.value has
      # all the text inside the comment and it can then count the number of new line characters in it.

      # Another alternative is to have t_htmlcomment_newline() which will count everything. And for errors simply do pass.

    def t_htmlcomment_end(self, t):
      r'-->'
      t.lexer.lineno += t.value.count('\n')
      t.lexer.begin('INITIAL')

    # Token defnitions for the javascript state:
    def t_javascript(self, t): # This name could be anything. This is actually an INITIAL token definition. But it should be put at the beginning so that it is considered first and then the control goes to the javascript states immediately without going into the INITIAL state.
      r'\<script[\ ]+type=\"text\/javascript\"\>' # this space cannot be ignored, hence it is escaped.
      t.lexer.code_start = t.lexer.lexpos # code_start is a custom variable.
      t.lexer.begin('javascript')

    t_javascript_ignore = ' \t\v\r'

    def t_javascript_error(self, t):
      t.lexer.skip(1)

    def t_javascript_end(self, t):
      r'<\/script>'
      t.lexer.lineno += t.value.count('\n')
      t.value = t.lexer.lexdata[t.lexer.code_start:t.lexer.lexpos-9] # delete the script tags.
      t.type = 'JAVASCRIPT'
      t.lexer.begin('INITIAL')
      return t

    # Token definitions for INITIAL state:
    def t_LANGLESLASH(self, t):
      r'</'
      return t

    def t_LANGLE(self, t):
      r'<'
      return t

    def t_RANGLE(self, t):
      r'>'
      return t

    def t_STRING(self, t):
      r'(?:\'[^\']*\')|(?:\"[^\"]*\")'
      t.value = t.value[1:-1]
      return t

    def t_WORD(self, t):
      r'[^ <>=\v\r\t\n]+'
      return t

    def t_EQUAL(self, t):
      r'-?[0-9]+'
      return t

    # Handle line numbers:
    def t_newline(self, t):
      r'\n+'
      t.lexer.lineno += len(t.value)
      pass

    # Handle whitespace by ignoring them:
    t_ignore = ' \t' # \n was already handled. We are handling tab and space over here.

    # Handle illegal or not-found keywords:
    def t_error(self, t):
      t.lexer.skip(1)

    # Building the lexer:
    def build(self):
      self.htmllex = lex.lex(module=self)

    # Input into the lexer:
    def sendInput(self, input_data):
      self.htmllex.input(input_data)

    # Output the result:
    def showOutput(self):
      while True:
        tok = self.htmllex.token()
        if not tok:
          break
        print tok.value

# Testing the class
# input = """<html>This is a <b> sample html file </b> and hope this works </html>"""
# my = HtmlLexer()
# my.build()
# my.sendInput(input) # Easier if the input is a triple quoted string instead of a single quoted. This may prevent problems appearing with strings type tokens.
# my.showOutput()
