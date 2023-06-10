from functools import reduce
from operator import add

if __name__ == '__main__':
    print(reduce(add, range(100)))
    print(sum(range(100)))

    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=lambda word: word[::-1]))

    print([callable(obj) for obj in (abs, str, 13)])