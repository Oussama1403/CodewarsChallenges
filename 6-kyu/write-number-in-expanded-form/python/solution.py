def expanded_form(num):
    num = list(str(num))
    l = []
    for i in range(len(num)):
        if num[i] != '0':
            zero = '0' * len(num[i+1::])
            f = str(num[i]) + str(zero)
            l.append(f)
    return " + ".join(l)    