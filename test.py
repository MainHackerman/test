string = "zaplati  Pepa  za 1000.0 piv 10 korun."
parts = string.split()
isnum = list()
nums = list()

name = "Pepa"
solution = [1000.0, 10.0]
correct = bool()
correct_name = False

for item in parts:
    if item == name:
        correct_name = True
    try:
        float(item)
        isnum.append(True)
        nums.append(float(item))
    except:
        isnum.append(False)

# JUDJING
if len(nums) != 2:
    print("FAIL - Wrong output string - not enought numbers")
    quit()

if nums[0] == solution[0] and nums[1] == solution[1]:
    correct = True
elif nums[0] == solution[1] and nums[1] == solution[0]:
    correct = True
else:
    correct = False

print(correct)
print(correct_name)
