string = "Pepa  zaplati za  10.0  piv  1000  korun."
parts = string.split()
isnum = list()

for item in parts:
    try:
        float(item)
        isnum.append(True)
    except:
        isnum.append(False)

