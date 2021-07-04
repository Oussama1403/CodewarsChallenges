def next_bigger(n):
    n = list(str(n))
    n = [int(x) for x in n]
    if sorted(n,reverse=True) == n:
        return -1
    else:    
        for i in range(1,len(n)):
            if n[-i] > n[-(i+1)]:
                listslice2 = n[-(i+1)+1::]
                bignums = [x for x in listslice2 if x > n[-(i+1)] ]
                bignum = min(bignums)
                indx = n.index(bignum,-i)
                n[-(i+1)],n[indx] = n[indx],n[-(i+1)]
                listslice2 = n[-(i+1)+1::]
                listslice1 = n[:-(i+1)+1]
                ascorder = sorted(listslice2) 
                n = listslice1 + ascorder 
                n = [str(x) for x in n]
                n = "".join(n)
                return int(n)