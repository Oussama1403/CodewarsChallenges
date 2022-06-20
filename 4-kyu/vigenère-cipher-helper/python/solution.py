import pytest
from itertools import cycle

class VigenereCipher (object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    def cipher(self, mode,str):
        word = ""
        for m,k in zip(str,cycle(self.key)):
            if m in self.alphabet:
               word = word + self.alphabet[(self.alphabet.index(m) +mode * self.alphabet.index(k)) % len(self.alphabet)]
            else:
               word = word + m   
        return word            
    def encode(self, str): return self.cipher(1, str)
    def decode(self, str): return self.cipher(-1, str)

# testing 

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'
c = VigenereCipher(key,alphabet)

def test_cipher():
    assert c.encode('codewars') == 'rovwsoiv'
    assert c.decode('rovwsoiv') == 'codewars'
    assert c.encode('waffles') == 'laxxhsj'
    assert c.decode('laxxhsj') == 'waffles'
    assert c.encode('CODEWARS') == 'CODEWARS'
    assert c.decode('CODEWARS') == 'CODEWARS'
    assert c.encode("it's a shift cipher!") == "xt'k o vwixl qzswej!"
