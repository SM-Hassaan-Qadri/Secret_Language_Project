# Encoder
text = input("Enter Text To Be Encoded >")
secreat_key = {
    "A" : "L" ,
    "B" : "K" ,
    "C" : "V" ,
    "D" : "W" ,
    "E" : "U" ,
    "F" : "I" ,
    "G" : "M" ,
    "H" : "S" , 
    "I" : "F" ,
    "J" : "Q" ,
    "K" : "B" ,
    "L" : "A" ,
    "M" : "G" ,
    "N" : "X" ,
    "O" : "P" ,
    "P" : "O" ,
    "Q" : "J" ,
    "R" : "Z" ,
    "S" : "H" ,
    "T" : "Y" ,
    "U" : "E" ,
    "V" : "C" ,
    "W" : "D" ,
    "X" : "N" ,
    "Y" : "T" ,
    "Z" : "R" ,
}


def encode(text):
    encoded = ""  # create new empty string to build encoded text
    for char in text.upper():
        if char in secreat_key:
            encoded += secreat_key[char]
        else:
            encoded += char  # keep spaces/punctuation
    return encoded


print(encode(text))


secreat_key2 = {
    "L": "A",
    "K": "B",
    "V": "C",
    "W": "D",
    "U": "E",
    "I": "F",
    "M": "G",
    "S": "H",
    "F": "I",
    "Q": "J",
    "B": "K",
    "A": "L",
    "G": "M",
    "X": "N",
    "P": "O",
    "O": "P",
    "J": "Q",
    "Z": "R",
    "H": "S",
    "Y": "T",
    "E": "U",
    "C": "V",
    "D": "W",
    "N": "X",
    "T": "Y",
    "R": "Z",
}

def decode(text):
    decoded = ""
    for char in text.upper():
        if char in secreat_key2:
            decoded += secreat_key2[char]
        else:
            decoded += char
    return decoded

code = int(input("Enter Password To Translate > "))

if code == 12123:
    text = input("Enter Text To Decode > ")
    print("Decoded:", decode(text))

else:
    print("Wrong Pin") 
