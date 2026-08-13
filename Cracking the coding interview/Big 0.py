#quick sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()  
        
        items_greater = []  
        items_smaller = []
        
        for item in arr:
            if item < pivot:
                items_smaller.append(item)
            else:
                items_greater.append(item)
        
        return quick_sort(items_smaller) + [pivot] + quick_sort(items_greater)
    
# arr = [10,9,8,7,6,5,4,3,2,1]
# sorted_arr = quick_sort(arr)
# print(sorted_arr)

# optimized quick_sort
# middle pivot often produces better results
# select pivot without removing it
# use list commprehension
#    import random

        # def quick_sort(arr):
        #     if len(arr) <= 1:
        #         return arr
        #     else:
        #         pivot_index = random.randint(0, len(arr) - 1)  # Random pivot selection
        #         pivot = arr[pivot_index]
        #         arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]  # Move pivot to end for partitioning
                
        #         items_smaller = [item for item in arr[:-1] if item < pivot]
        #         items_greater = [item for item in arr[:-1] if item >= pivot]
                
        #         return quick_sort(items_smaller) + [pivot] + quick_sort(items_greater)
