import string

alphabet = string.ascii_lowercase

def decrypt(message):
    for s in range(26):
        message_shifted = ""
        for c in message:
            if c in alphabet:
                pos = alphabet.find(c)
                pos_new = (pos - s) % 26
                c_new = alphabet[pos_new]
                message_shifted += c_new
            else:
                message_shifted += c
        print("Shift #" + str(s) + ": " + message_shifted)

decrypt(input("Enter message to decrypt: ").lower())