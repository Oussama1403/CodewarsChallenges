import re
def increment_string(s):
    if not s == "":
        if not s.isalpha():
            d = re.search(r'\d+$', s)
            if d == None:
                return s + "1"
            
            z = re.search(r'^0+',d.group())
            if z == None:
                return s.split(d.group())[0] + str(int(d.group())+1)
            else:
                if len( str( (int(d.group())+1) ) + "0"*len(z.group()) ) > len(d.group()):
                    number = "0"*(len(z.group())-1) + str(int(d.group())+1)
                    return s.split(d.group())[0] + number
                else:
                    number = "0"*len(z.group()) + str(int(d.group())+1)
                    return s.split(d.group())[0] + number
            
    return s + "1"