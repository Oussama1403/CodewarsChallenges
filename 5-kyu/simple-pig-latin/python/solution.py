def pig_it(text):
    l = []
    for word in text.split():
        if word.isalpha():
            o = word[1:]+word[0] +  "ay"
            l.append(o)
        else:
            l.append(word)    
    return " ".join(l)  