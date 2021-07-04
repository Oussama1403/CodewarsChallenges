def create_phone_number(n):
    l = [str(x) for x in n]
    num  = "".join(l)
    num = "("+num[0:3]+")"+" "+num[3:6]+"-"+num[6::]
    return num 