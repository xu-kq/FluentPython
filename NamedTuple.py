from collections import namedtuple
City = namedtuple('city', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.68722, 139.691667))

print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delphi_data = ('Delphi NCR', 'IN', 21.935, LatLong(28.61, 77.21))
delphi = City._make(delphi_data)
print(delphi._asdict())
print(delphi._asdict().items())

for key, val in delphi._asdict().items():
    print(key+':', val)
