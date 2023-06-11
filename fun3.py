from inspect import signature


def clip(text: str, maxlen:'int > 0'=80)-> str:
    """Return text clipped at the last space before or after max_len"""
    end = None
    if len(text) > maxlen:
        space_before = text.rfind(' ', 0, maxlen)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.find(' ', maxlen)
            if space_after >=0:
                end = space_after

    if end is None:
        end = len(text)
    return text[:end].rstrip()


if __name__ == '__main__':
    print(clip.__defaults__)
    print(clip.__code__.co_varnames)
    print(clip.__code__.co_argcount)

    sig = signature(clip)
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)

    print(repr(clip.__annotations__))