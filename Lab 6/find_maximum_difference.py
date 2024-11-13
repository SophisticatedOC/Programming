# def find_maximum_difference(a, b):
#     # code implementation here...

def find_maximum_difference(l1, l2):
    mx1 = max(l1)
    mn1 = min(l1)
    mx2 = max(l2)
    mn2 = min(l2)
    
    diff1 = abs(mx1 - mn2)
    diff2 = abs(mx2 - mn1)
    
    return max(diff1, diff2)

print(find_maximum_difference([1, 5, 600], [100, 7, 3, 29, 39]))