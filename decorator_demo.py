# Actually equal to:
# def deco(func):
#     def inner():
#         print('running inner()')
#     return inner
# def target():
#     print('running target')
# target = deco(target)
def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target')

if __name__ == '__main__':
    target()
    print(target)
