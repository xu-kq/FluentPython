symbols = '$¢£¥€¤'
# 1. list comps
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

# 2. map and filter
beyond_ascii = list(filter(lambda c: c > 127, map(ord,symbols)))
print(beyond_ascii)

#3. genexpr
print(\
    tuple(ord(symbol) for symbol in symbols)
    )
import array
print(
    array.array('I', (ord(symbol) for symbol in symbols))
)