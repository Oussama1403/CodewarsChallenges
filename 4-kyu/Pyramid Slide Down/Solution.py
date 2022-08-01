def longest_slide_down(pyramid):
    q = [pyramid[-1]]
    while q != []:
        n = q.pop(0)
        indx = pyramid.index(n)
        if len(n) == 1:
            return n[0]
        n = [max(n[i],n[i+1]) for i in range(len(n)-1)]
        pyramid[indx-1] = [a+b for a,b in zip(n,pyramid[indx-1])]
        q.append(pyramid[indx-1])

x = longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) 
assert x == 23 , f'Error, got {x} instead of 23'
