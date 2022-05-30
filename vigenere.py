#!/usr/bin/python3

import sys
from collections import Counter

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}


def decrypt(str,key):
    value = ""
    for i in range(len(str)):
        index1 = ord(str[i]) - ord('A')
        final = index1 - key
        
        if final<0:
            final +=26
        value +=alphabet[final]
    return value

def chi_square(s):
    freqs = Counter(s)
    return sum(((float(freqs[c])/len(s)) - letter_freqs[c])**2/ (letter_freqs[c]) for c in freqs)


def encrypt(str, key):
    alph1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str = str.upper()
    repeat = (len(str)//len(key))+1
    key = key *repeat
    key = key[:len(str)]
    key = key.upper()
    

    value = ""
    for i in range(len(str)):
        if str[i] == " ":
            continue
        ind1 = ord(str[i]) - ord('A')
        ind2 = ord(key[i]) - ord('A')
        sum = (ind1+ind2)%26
        value = value + alph1[sum]
    return value


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs) 
    return sum(((float(freqs[c])/len(s))-mean)**2 for c in freqs)/len(freqs)
    


def find_mean(str, key):
    temp = 0
    variance = 0
    for i in range(key):
        temp = ''
        while i<len(str):
            temp += str[i]
            i+=key
        variance += float(pop_var(temp))
    variance = float(variance/key)

    return variance


def find_word(str, n):
    words = []
    for i in range(n):
        temp = ""
        while i < len(str):
            temp += str[i]
            i+=n
        words.append(temp)
    final_word = []
    for word in words:
        chisquare_values = []
        for i in range(26):
            decrypt_word = decrypt(word,i)
            chisquare_values.append(chi_square(decrypt_word))
        final_word.append(alphabet[chisquare_values.index(min(chisquare_values))])
    return ''.join(final_word)



if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()
    alph = [0 for x in range(26)]
    n = 0
    for i in range(2,14):
        temp.append(find_mean(cipher,i))
    for y in range(len(temp)):
        if temp[y]>= 0.001:
            n=y+2
            break

    print(find_word(cipher, n))

