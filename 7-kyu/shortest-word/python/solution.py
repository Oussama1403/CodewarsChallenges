def find_short(s):
    s = s.split()
    minn = len(s[0])
    for i in range(len(s)-1):
        if len(s[i+1]) < minn :
            minn = len(s[i+1]) 
    return minn