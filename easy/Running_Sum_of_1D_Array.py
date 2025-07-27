

def runningSum(l):
    output = []
    s = 0
    for i in l:
        s = s + i
        output.append(s)

    return output

print(runningSum([3,1,2,10,1]))