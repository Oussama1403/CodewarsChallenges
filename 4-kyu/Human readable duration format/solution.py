def format_duration(seconds):
    if seconds == 0:return "now"

    y = ( (x:=(seconds // (3600 * 24 * 365))) , " years" if x > 1 else " year"  )
    d = ( (x:=(seconds%(3600 * 24 * 365)) // (3600 * 24)) , " days" if x > 1 else " day"  )
    
    h = ( (x:=(seconds // 3600 % 24)) , " hours" if x > 1 else " hour" )
    m = ( (x:=(seconds % 3600 // 60)) , " minutes" if x > 1 else " minute" )
    s = ( (x:= (seconds % 3600 % 60)) , " seconds" if x > 1 else " second" )
    
    f = list(filter(lambda t:t[0] > 0,[y,d,h,m,s]))
    time = ""
    for u in f[:-1]:
        time = time + str(u[0]) + u[1]+", "
    time = (time.rstrip(", ") + " and " + str(f[-1][0]) + f[-1][1].rstrip()) if time != "" else str(f[-1][0]) + f[-1][1].rstrip()
    return time

# TOP SOLUTION

times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]

