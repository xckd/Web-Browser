import ply.lex as lex

tokens = (
    'spacetext',
    'number',
)

t_ignore = '\t\v\r' # the last character is a space.
def t_spacetext(t):
  r'\ [a-z]+'
  return t

def t_number(t):
  r'[0-9]+'
  return t

def t_error(t):
  print "Illegal character '%s'" % t.value[0]
  # print t.lexer.lexdata
  t.lexer.skip(1)


lexer = lex.lex()
lexer.input("""  an ox \t 256\n   """)
print "Ignored characters are \\t\\v\\r and space"
while True:
  tok = lexer.token()
  if not tok: break
  print tok

1. Everytime the .token() is called, t_ignore rule is executed and all the characters trimmed from the
beginning of the input stream.
2. When a character matches a rule, all the subsequent characters are matched with the same rule
untill one of the characters doesn't match.
  i. if it doesn't match and we are already in an accepting state, it will be returned to the environment calling
      the .token function and lexing would start from this point when the next call to the .token() is made.
      Note: The lexdata remains the same throughout the lexing process. The t_ignore rules doesn't mutate the
            lexdata.
  ii. if it doesn't match and we are not in an accepting state, the first character from that .token() call will
      be matched with the subsequent rules and the process continues.
  iii.if the character doesn't match with any of the rules, then t_error is triggered and the process is again
      started automatically after skipping n number of characters mentioned in lexer.skip(n) function call.
      Note: lexer.skip(n) is an essential component in the t_error string specification. without this, the process
      of lexing will not continue on its own.
      We cannot replace this statement with pass as that wouldn't tell the lexer to begin the process again.

      This was the difference between lexer.skip(n) and pass.
