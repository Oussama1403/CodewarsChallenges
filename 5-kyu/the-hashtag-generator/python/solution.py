def generate_hashtag(s):
    if not (len(s) == 0):
        s = s.split()
        for word in s:
            if len(word) > 140:
                return False
            else:
                s = [word.capitalize() for word in s]
                return "#" + "".join(s)
    else:
        return False