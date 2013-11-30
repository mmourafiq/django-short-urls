# -*- coding: utf-8 -*-
DEFAULT_ALPHABET = 'az7er5tyu1io0pq4sd9fg6hjk8lmw3xcv2bn'
LEGTH_GENERATION = 32
MIN_LENGTH = 6

class URLEncoder(object):
    """
    It generates 36**6 = 2176782336 values (6 lowercase letters) which falls between 2**31 = 2147483648 and 2**32 = 4294967296.
    It pads the codes that are shorter than 6 characters with leading 'a' characters,     
    """
    def __init__(self, alphabet=DEFAULT_ALPHABET, length_generation=LEGTH_GENERATION):
        self.alphabet = alphabet
        self.length_generation = length_generation
        self.mask = (1 << length_generation) - 1
        self.mapping = range(length_generation)
        self.mapping.reverse()
        
    def encode_url(self, n, min_length=MIN_LENGTH):
        return self.__enbase(self.__encode(n), min_length)
    
    def decode_url(self, n):
        return self.__decode(self.__debase(n))
    
    def __encode(self, n):
        result = 0
        for i, b in enumerate(self.mapping):
            if (n & self.mask) & (1 << i):
                result |= (1 << b)
        return (n & ~self.mask) | result
    
    def __decode(self, n):
        result = 0
        for i, b in enumerate(self.mapping):
            if (n & self.mask) & (1 << b):                
                result |= (1 << i)
        return (n & ~self.mask) | result    
    
    def __enbase(self, x, min_length=MIN_LENGTH):
        result = self.__enbase_iter(x)
        padding = self.alphabet[0] * (min_length - len(result))
        return '%s%s' % (padding, result)
    
    def __enbase_iter(self, x):
        n = len(self.alphabet)
        if x < n:
            return self.alphabet[x]
        return self.__enbase_iter(x / n) + self.alphabet[x % n]
    
    def __debase(self, x):
        n = len(self.alphabet)
        result = 0
        for i, c in enumerate(reversed(x)):
            result += self.alphabet.index(c) * (n ** i)
        return result
