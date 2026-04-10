#Calc Inputs
num1 = 2
num2 = 9
num3 = '^'

#Imports
import math

#calculator
def calc(a,b,c):
    if c == '+' or c == 'plus' or c == 'add':
        print(a,'+',b,'=',a + b)
    elif c == '-' or c == 'minus' or c == 'subtract':
        print(a,'-',b,'=',a - b)
    elif c == '*' or c == 'times' or c == 'multiply by':
                print(a,'x',b,'=',a * b)
    elif c == '/' or c == 'divide':
        print(a,'/',b,'=',a / b)
    elif c == 'square root of' or c == 'root':
        print(a,'√',b,'=',a * math.sqrt(b))
    elif c == '^' or c == 'to the power of' or c == 'power':
        def tosmall(num):
            if num == 0:return '⁰'
            elif num == 1:return '¹'
            elif num == 2:return '²'
            elif num == 3:return '³'
            elif num == 4:return '⁴'
            elif num == 5:return '⁵'
            elif num == 6:return '⁶'
            elif num == 7:return '⁷'
            elif num == 8:return '⁸'
            elif num == 9:return '⁹'
            else:return
        if tosmall(b) == None:
            print(a,'^',b,'=',pow(a,b))
        else:
            print(a,tosmall(b),'=',pow(a,b))
    else:
        return ''
        

#run calc
calc(num1,num2,num3)