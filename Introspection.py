def factional(n):
    '''return n!'''
    return 1 if n < 2 else n * factional(n - 1)


def upper_acse_name(obj):
    return("%s %s".format(obj.first_name, obj.last_name).upper())
upper_acse_name.short_description = 'Customer name'


class C:
    pass


def func(): pass


if __name__ == '__main__':
    obj = C()
    print(sorted(set(dir(func)) - set(dir(obj))))
    print(upper_acse_name.__code__)
