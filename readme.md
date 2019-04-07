# LL(1) Parser (Compiler Design)

This is a LL(1) parser for Switch Statements written in Python3,
the first, follow set and Parse table for the Grammer can be generated using this [link](http://jsmachines.sourceforge.net/machines/ll1.html)

## Language

```
int main()
	char operator;
	int firstNumber , secondNumber;

	switch(operator)
	begin    
		case '+':
		printf(firstNumber + secondNumber);
		break;
		case '-':
            	printf(firstNumber - secondNumber);
		break;
		default:
			printf( firstNumber + firstNumber);
			break;
        end 
return 0;
```
## Grammer

```
S -> T MAIN ( ) B RETURN VAL ;
B -> D B'
B' -> SW 
B' -> ''
D -> T ID L ; D
D -> ''
L -> , ID L
L -> ''
T -> INT
T -> CHAR
T -> FLOAT
SW -> SWITCH ( ID ) BEGIN ST END
ST -> C ST'
ST' -> DEF 
ST' -> ''
C -> CASE VAL : E C
C -> BREAK ; C 
C -> ''
DEF -> DEFAULT : E BREAK ;
E -> PRINT ( ID OP ID ) ;
VAL -> ID
VAL -> NUM
```

## Usage

```bash
python3 parser.py <filename> #For testing you can use a.lang which is valid input
```