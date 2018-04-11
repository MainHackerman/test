string = "Pepa  zaplati za  10.0  piv  1000  korun."
parts = string.split()


def isnumber(teststr):
    return teststr.isdigit() or teststr.isnumeric() or teststr.isdecimal()


isnum = list()
for item in parts:
    isnum.append(isnumber(item))
    print(item, item.isdigit())

print(isnum)
decim = "10.02"
print(decim.isdecimal())