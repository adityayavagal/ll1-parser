#!/usr/bin/python3

from lexer import lex
import sys
import pandas as pd
import numpy as np

terminals = ["MAIN", "(", ")", "RETURN", ";", "ID", ",", "INT", "CHAR", "FLOAT",
             "SWITCH", "BEGIN", "END", "CASE", ":", "BREAK", "DEFAULT", "PRINT", 
             "OP", "NUM", "$"]
non_terminals = ["S", "B", "B'", "D", "L", "T", "SW", "ST", "ST'", "C", "DEF", "E", "VAL"]

data = [
    ["-", "-", "-", "-", "-", "-", "-", "T MAIN ( ) B RETURN VAL ;", "T MAIN ( ) B RETURN VAL ;", "T MAIN ( ) B RETURN VAL ;", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "D B'", "-", "-", "-", "D B'", "D B'", "D B'", "D B'", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "", "-", "-", "-", "-", "-", "-", "SW", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "", "-", "-", "-", "T ID L ; D", "T ID L ; D", "T ID L ; D", "", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "", "-", ", ID L", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "INT", "CHAR", "FLOAT", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "SWITCH ( ID ) BEGIN ST END", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "C ST'", "C ST'", "-", "C ST'", "C ST'", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "", "-", "-", "-", "DEF", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "", "CASE VAL : E C", "-", "BREAK ; C", "", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "DEFAULT : E BREAK ;", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "PRINT ( ID OP ID ) ;", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "ID", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "NUM", "-"]
]

table = pd.DataFrame(data, columns=terminals, index=non_terminals)
tokens = []
stack = ["$", "S"]
i = 0
if(len(sys.argv)!=2):
	print("Usage: ./lex.py [FileName]")
	sys.exit(1)

tokens = lex(sys.argv[1])
print(tokens)
print("Parsing...")
print()
print("MATCH".center(20), "Stack TOP".center(20), "INPUT TOKEN".center(20))
while(stack[-1] != "$" and i != len(tokens)):
    top = stack.pop()

    if top in non_terminals:
        prods = table.loc[[top], [tokens[i]]].values[0].tolist()[0].split(' ')
        for prod in range(len(prods)-1, -1, -1):
            stack.append(prods[prod])

        print("Not Match".center(20), top.center(20), tokens[i].center(20))#, tokens[i].center(30)

    elif top == "":
        continue
    else:
        if top == tokens[i]:
            print("Match: ".center(20), top.center(20),  tokens[i].center(20))
            i += 1
            
        else:
            print()
            print("==========================")
            print("Stack:", stack)
            print("Parsing Failed")
            print("==========================")
            sys.exit(1)

print()
print("==========================")
print("Stack:", stack)
print("Parsing Success")
print("==========================")