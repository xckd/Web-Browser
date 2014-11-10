Let the whole page be called html:
<b> Welcome to <i> my </i> webpage ! </b>
The html is a combination of words and tags called element.
That means it has an infinite number of elements which is shown
recursively in the following way:

html -> element html
html ->
element -> word
element -> tag-open html tag-close
# Within the tags, we have another list of elements or an entire webpage.

tag-open -> <word>
tag-close -> </word>

Grammar for javascript:
Expressions:
exp -> exp exp
exp -> exp exp
exp -> number

Statements:
stmt -> identifier = exp
stmt -> return exp
stmt -> if exp compoundstmt
stmt -> if exp compoundstmt else compoundstmt
compoundstmt -> {stmts}
stmts -> stmt; stmts
stmts ->

Functions:
(declare and call)
declaration of functions:
js -> element js
js ->
element -> function identifier (optparams) compoundstmt
element -> stmt;
optparams -> params
optparams ->
params -> identifier, params
params -> identifier

calling of functions:
exp -> identifier(optargs)
optargs -> args
optargs ->
args -> exp , args
args -> exp

Toosl to use in the parser:
1. Map
2. Lambda
3. List comprehensions
4. Generator: A function that has yield keyword in it to create a new function.
Generator function automatically returns the new list.
