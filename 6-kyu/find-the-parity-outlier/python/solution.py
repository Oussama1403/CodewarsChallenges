def find_outlier(integers):
    even = 0
    odd = 0
    e = 1
    o = 1
    for n in integers:
        if n % 2 == 0:
            even = even + e
            e+=1
        else:
            odd = odd + o
            o+=1
    oddnum = 0
    evennum = 0    
    if even > 1:
        for n in integers:
            if n % 2 != 0:
                oddnum = n
        return oddnum         
    else:
        for n in integers:
            if n % 2 == 0:
                evennum = n
        return evennum