"""
Nouvel encryptage.
"""
from constantes import hex_char

class Crypto():

    def __init__(self):
        pass

    def encrypt(self, chaine):
        key = 0
        chaine = chaine.encode().hex()
        e_chaine = ''
        for char in chaine:
            if char in hex_char:
                place = hex_char.index(char) + key
                if place < len(hex_char):
                    e_chaine += hex_char[place]
                else:
                    index = place%len(hex_char)
                    e_chaine += hex_char[index]
            else:
                print('Probleme.')
            key+=1
        return e_chaine

    def decrypt(self, e_chaine):
        key = 0
        chaine = ''
        for char in e_chaine:
            if char in hex_char:
                place = hex_char.index(char) - key
                if place >= 0:
                    if place < len(hex_char):
                        chaine += hex_char[place]
                    else:
                        print('Probleme A.')
                else:
                    while place < 0:
                        place += len(hex_char)
                    chaine += hex_char[place]
            else:
                print('Probleme B.')
            key += 1
        return bytes.fromhex(chaine).decode()


if __name__ == '__main__':
    e = Crypto()
    i = e.encrypt('coucou comment tu vas ?')
    print(i)
    v = e.decrypt('6482bacae810ed426080a2cce71fed537643bbc8fccbfc')
    print(v)
