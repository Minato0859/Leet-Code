from linear_search import verify

def binary_search(list, target):
    first = 0
    last = len(list) - 1
    
    
    while first <= last:
        midpoint = (first + last) // 2
        
        if list[midpoint] ==  target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    
    return None

if __name__ == "__main__":        

    numbers = [i for i in range(9)]

    result = binary_search(numbers, 8)
    verify(result)