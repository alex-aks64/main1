def test1(a,b,c):
    print(a,b,c)
d = [2,'hi',True]
test1(*d)


def recursion():

    recursion()
stack = []
stack.append(1)
print('Добав' , stack)
stack.append(2)
print('Добав' , stack)
stack.append(3)
print('Добав' , stack)
stack.append(4)
print('Добав',stack)
stack.append(5)
print('Добав',stack)
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)

