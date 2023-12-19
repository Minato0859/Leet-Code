# x = [1,2,3]
# print(id(x))

# y = x

# x.append(4)

# print(x, y)
# print(id(y))

#  Deep Copy

def deep_copy_1(x):
    y =[]
    for e in x:
        new_e = []
        for sub_e in e:
            new_e.append(sub_e)
        y.append(new_e)
    y[0][0] = 5
    
    
    print(id(x))
    print(id(y))
    print(id(a))

# a = [[1,2], [3,4], [5,6]]
# deep_copy_1(a)
# print(a)
# print(id(a))


def deep_copy_2(x):
    y =[]
    for e in x:
        new_e = e[:]
        y.append(new_e)
    y[0][0] = 5
    
    
    
    print(id(x))
    print(id(y))


# a = [[1,2], [3,4], [5,6]]
# deep_copy_2(a)
# print(a)
# print(id(a))