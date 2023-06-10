def factional(n):
    '''return n!'''
    return 1 if n < 2 else n * factional(n - 1)


if __name__ == '__main__':
    print(factional(42))
    print(factional.__doc__)
    print(type(factional))
