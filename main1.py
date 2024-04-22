def test1(a):
    print(a)
    print(a)
d = ['hi']
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

def sum(n):
    if n != 0:
        return n + sum(n-1)
    else:
        return 0


print(sum(6))
