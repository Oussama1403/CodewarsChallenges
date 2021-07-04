function firstNonRepeatingLetter(s) {
    let newstr = s.toLowerCase();
    let i;
    for (i=0;i<s.length;i++) {
        if (! ( (newstr.split(newstr[i]).length - 1) > 1 ) ) {
            return s[i];
        }
    }
    return "";
}