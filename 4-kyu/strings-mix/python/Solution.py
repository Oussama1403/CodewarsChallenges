def sort(ch):
    for i in range(len(ch)):
        for j in range(i+1,len(ch)):
            if len(ch[i]) < len(ch[j]):
                ch[i],ch[j]=ch[j],ch[i]
            if len(ch[i]) == len(ch[j]):
                if ch[i] > ch[j]:
                    ch[i],ch[j]=ch[j],ch[i]
    return ch            
def mix(s1, s2):
    ch = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    for alpha in letters:
        if alpha in s1 or alpha in  s2:
            if s1.count(alpha) > s2.count(alpha) and not s1.count(alpha) <= 1  :
                ch = ch + "1:"+(alpha*s1.count(alpha))+"\\" 
            elif s1.count(alpha) < s2.count(alpha) and not s2.count(alpha) <= 1:
                ch = ch + "2:"+(alpha*s2.count(alpha))+"\\" 
            else:
                if not s1.count(alpha) <= 1:ch = ch + "=:"+(alpha*s1.count(alpha))+"\\" 
    print("ch : ",ch)
    ch = ch.split("\\")[:-1]
    ch = sort(ch) # sort string by length
    return "\\".join(ch)      
    
#s1 = "my&friend&Paul has heavy hats! &"
#s2 = "my friend John has many many friends &"
#s = mix(s1,s2)
#print("s =",s)
s1="Sadus:cpms>orqn3zecwGvnznSgacs"
s2="MynwdKizfd$lvse+gnbaGydxyXzayp"
s = mix(s1,s2)
print("s =",s)


