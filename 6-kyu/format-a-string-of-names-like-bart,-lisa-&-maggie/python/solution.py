def namelist(names):
    if len(names) == 0:
        return ''      
    l = []
    for i in range(len(names)):
        l.append(names[i]["name"])
    if len(l) == 1:
        return l[0]
    else:        
        return ", ".join(l[0:-1])+" & "+l[-1]