from Stack1 import Stack1


stack = Stack1()
stack2 = Stack1()
stack3 = Stack1()
n = 0
sequencia = str(input("Digite a sequencia de caracteres: "))

for expressao in sequencia:
    
    stack.push(sequencia[n]) 
    stack3.push(sequencia[n]) 
    n += 1
for n in range(stack._size):
    stack2.push(stack.top.data)
    print(stack2.top.data)
    stack.pop()
for n in sequencia:
        if (stack3.peek() == stack2.peek()):
            print(stack3.peek())
            print(stack2.peek())
            stack3.pop()
            stack2.pop()
        
if stack3._size == 0 and  stack2._size == 0:
    print("A sequencia é um palindrom")
else:
    print("Não é palindromo")                 
