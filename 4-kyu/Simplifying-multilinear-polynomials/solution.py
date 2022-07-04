import re

def calc(s):
    s = re.split("([\+\-])+",s)
    s = [c for c in s if c != '']
    for i in range(len(s)):
        s[i] = re.sub("[a-z]","",s[i])
    s = ['1' if c == '' else c for c in s]
    return eval("".join([c for c in s]))

def simplify(eq):
    s = re.findall(r'[+\-]?\d*[a-z]+', eq)
    s = ["+"+c if "+" not in c and "-" not in c else c for c in s]
    print(s)
    s = sort(s)
    result = ""
    for c in range(len(s)):
        l = [s[c]]
        m = re.findall("[a-z]",s[c])
        for i in range(c+1,len(s)):
            if m == []:
                continue
            m2 = re.findall("[a-z]",s[i])
            if m == m2:
                l.append(s[i])
                s[i] = ''
        if l == [s[c]]:
            result = result + s[c]  
        else:     
            l = "".join(l) 
            sg = '+' if calc(l) > 0 else ''
            if calc(l) == 0:
                result = result + ""
            elif calc(l) == 1:
                result = result + sg+"".join(m)
            else:
                result = result + sg+str(calc(l))+"".join(m)
    if result[0] == "+":
        return result[1:] 
    return result

def sort(s):
    def sort_lexico(s):        
        for i in range(len(s)):
            m = re.findall("[a-z]",s[i])
            for j in range(i+1,len(s)):
                m2 = re.findall("[a-z]",s[j])
                if len(m) == len(m2):
                    if m > m2:
                        s[i],s[j]=s[j],s[i]
        return s                
    # sort each var
    for i,c in enumerate(s):
        coeff = re.findall("[a-z]",c)
        sortedcoeff = sorted(coeff)
        s[i] = s[i].replace("".join(coeff),"".join(sortedcoeff))
    # sort all by var length
    s = sorted(s,key=lambda x: len(''.join(i for i in x if not i.isdigit() and not i in ["+","-"]))) 
    # sort lexicographic
    s = sort_lexico(s)
    return s
