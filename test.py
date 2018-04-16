import os

def CreateDataSet(list):
    os.system('touch test_values')
    os.system('rm test_values')
    os.system('touch test_values')
    try:
        file = open('test_values')
        file.close()
    except:
        print('Cannot create file for test values - exiting test.')
        quit()

    for item in list:
        os.system("echo " + str(item) + " >> test_values")


def GetResults():
    os.system('python3 project.py < test_values > test')
    file = open('test')
    string = file.read()
    file.close()
    return string.split()


def ClearEnv():
    os.system('rm test')
    os.system('rm test_values')

test_val = [10, 100, 0, 100, 'Pepa']
CreateDataSet(test_val)
lst = GetResults()
ClearEnv()

solution = [1000.0, 10.0]
nums = list()

for item in lst:
    try:
        nums.append(float(item))
    except:
        pass

# JUDJING
if test_val[-1] in lst:
    print("PASS - Name of group leader in output string")
else:
    print("FAIL - Name of group leader NOT in output string")

if len(nums) != 2:
    print("FAIL - Wrong output string - not enought numbers")
    quit()

if (nums[0] == solution[0] and nums[1] == solution[1]) or (nums[0] == solution[1] and nums[1] == solution[0]):
    print("PASS - Numeric solution is correct")
else:
    print("FAIL - Wrong numeric solution")