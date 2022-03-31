from collections import deque
#se puede inicializar con deque
numbers=deque()
numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)

last_item=numbers.pop()
print(last_item)
print(numbers)

first_item=numbers.popleft()
print(first_item)
print(numbers)