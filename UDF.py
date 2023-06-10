import random


class BingoCase:
    def __init__(self, items):
        self._item = list(items)
        random.shuffle(self._item)

    def pick(self):
        try:
            return self._item.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCase')

    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCase(range(3))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))
