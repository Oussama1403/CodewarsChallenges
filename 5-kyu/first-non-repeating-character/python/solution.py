def first_non_repeating_letter(string):
    newstr = string.lower()
    for i in range(len(newstr)):
        if not newstr.count(newstr[i]) > 1:
            return string[i]
    return ""