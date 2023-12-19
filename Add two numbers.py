        
def addtwonumbers(l1, l2):
    
    x1 = ''
    x2 = ''
    for x, y in zip(l1[::-1], l2[::-1]):
        x1 += str(x)
        x2 += str(y)
    x1 = int(x1)
    x2 = int(x2)

    output = str(x1+x2)
    outputt = []
    for i in output[::-1]:
        outputt.append(int(i))

    return outputt

print(addtwonumbers([0, 0, 1], [0, 0, 2]))