import sys

fnout = open('negative.txt', 'w')
fpout = open('positive.txt', 'w')

def result(operand, a, b):
    if operand == '*':
        return a*b
    elif operand == '/':
        return a/b
    elif operand == '+':
        return a+b
    elif operand == '-':
        return a-b
def checkAndWrite(num):
    if num < 0: fnout.write(str(num)+'\n')
    else: fpout.write(str(num)+'\n')

try:
    file = open(sys.argv[1])
    operation = sys.argv[2]
except:
    print("File doesn\'t exist or wrong operation")

for line in file:
    a = line.rstrip().split(' ')
    foo = result(operation, int(a[0]), int(a[1]))
    checkAndWrite(foo)


        
            
    


