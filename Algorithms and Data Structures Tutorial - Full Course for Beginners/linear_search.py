def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
        
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in list')


if __name__ == '__main__':
            
    numbers = [i for i in range(1, 11)]

    result = linear_search(numbers, 12)
    verify(result)


    result = linear_search(numbers, 6)
    verify(result)