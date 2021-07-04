def anagrams(word, words):
    angrm = []
    for i in range(len(words)):
        f = 0
        for ch in words[i]:
            if not ( (ch in word) and ( word.count(ch) == words[i].count(ch) ) ):
                f = 1
        if not f == 1:
            angrm.append(words[i])             
    return angrm