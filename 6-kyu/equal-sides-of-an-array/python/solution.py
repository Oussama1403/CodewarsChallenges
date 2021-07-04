def find_even_index(arr):
    for n in range(len(arr)):
        leftside = arr[n+1::]
        rightside = arr[0:n]
        if sum(leftside) == sum(rightside):
            return n
    else:
        return -1    
