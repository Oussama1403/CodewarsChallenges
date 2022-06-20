class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    def encode(self, text):
        ch = ""
        if len(text) > len(self.key):self.key = self.key * len(text)
        for i in range(len(text)):
            if text[i] not in self.alphabet:ch = ch + text[i]
            else:
                index_txt = self.alphabet.index(self.key[i])
                index_key = self.alphabet.index(text[i])
                next_letter = self.alphabet[(index_txt+index_key)%len(self.alphabet)]
                ch = ch + next_letter
        return ch    
    def decode(self, text):
        ch = ""
        if len(text) > len(self.key):self.key = self.key * len(text)
        for i in range(len(text)):
            if text[i] not in self.alphabet:ch = ch + text[i]
            else:
                index_txt = self.alphabet.index(self.key[i])
                index_key = self.alphabet.index(text[i])
                next_letter = self.alphabet[(index_key-index_txt)%len(self.alphabet)]
                ch = ch + next_letter
        return ch
