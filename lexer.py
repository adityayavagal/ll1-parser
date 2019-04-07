#!/usr/bin/python3
import re

def lex(fileName):
    f=open(fileName, 'r')

    tokenlist = []

    operators = { '=': '=','+': '+', '-' : '-', '/' : '/', '*': '*', '++' : '++', '--' : '--'}
    optr_keys = operators.keys()

    datatype = {'int': 'INT','float' : 'FLOAT', 'char': 'CHAR', 'void' : 'VOID'}
    datatype_keys = datatype.keys()

    keyword = {'return' : 'RETURN', 'switch' : 'SWITCH', 'case' : 'CASE', 'break' : 'BREAK', 'begin' : 'BEGIN', 'end' : 'END', 'default' : 'DEFAULT'}
    keyword_keys = keyword.keys()

    delimiter = {';':';'}
    delimiter_keys = delimiter.keys()

    blocks = {'{' : '{', '}' : '}', '(' : '(', ')' : ')'}
    block_keys = blocks.keys()

    builtin_functions = {'printf':'PRINT', 'main' : 'MAIN', 'scanf' : 'SCAN'}

    non_identifiers = ['_','`','~','!','@','#','$','%','^','&','*','(',')','=','|','"',':','{'
    ,'}','[',']','<','>','?','/', ',']

    operators = ['-', '+', '/', '*']

    numerals = ['0','1','2','3','4','5','6','7','8','9','10']

    insert_space = re.compile(r"([<(,=*/%;:)>])")

    i = f.read()

    dataFlag = False

    count = 0
    program = i.split('\n')

    for line in program:
        if line == '':
            continue
        count += 1
        # print("Line #" +  str(count))
        # print("Line :", line)
        line = insert_space.sub(" \\1 ", line)
        line = re.sub(r'\t', '', line)
        tokens = line.split(' ')
        #print(tokens)
        
        for token in tokens:
            token = token.strip('')
            if token == '':
                continue

            if token in builtin_functions.keys():
                tokenlist.append(builtin_functions[token])
                # print(builtin_functions[token])

            elif token in block_keys:
                tokenlist.append(blocks[token])
                # print(blocks[token])

            elif token in optr_keys:
                tokenlist.append("OP")
                # print("OP")

            elif token in non_identifiers:
                tokenlist.append(token)
                # print(token)

            elif token in delimiter:
                tokenlist.append(delimiter[token])
                # print(delimiter[token])

            elif token in datatype_keys:
                tokenlist.append(datatype[token])
                # print(datatype[token])

            elif token in keyword_keys:
                tokenlist.append(keyword[token])
                # print(keyword[token])

            elif token in numerals:
                tokenlist.append("NUM")
                # print("NUM")

            elif (token not in non_identifiers) and ('()' not in token):
                tokenlist.append("ID")
                # print("ID")
            

        dataFlag = False

    # print("Done")
    f.close()
    return tokenlist
