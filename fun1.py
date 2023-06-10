def factional(n):
    '''return n!'''
    return 1 if n < 2 else n * factional(n - 1)


def reverse(word):
    return word[::-1]


if __name__ == '__main__':
    fact = factional
    print(list(map(fact, range(11))))

    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=len))

    print(reverse('testing'))

    print(list(map(fact, filter(lambda n: n % 2, range(6)))))
    print([fact(i) for i in range(6) if i % 2])