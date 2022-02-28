import string

#Chi Squared Test by TheAlgorithms/Python/ciphers/decrypt_caesar_with_chi_squared.py

alphabet = string.ascii_lowercase #Array of lowercase alphabetical characters
frequencies = { #Frequencies of English language
    "a": 0.08497,
    "b": 0.01492,
    "c": 0.02202,
    "d": 0.04253,
    "e": 0.11162,
    "f": 0.02228,
    "g": 0.02015,
    "h": 0.06094,
    "i": 0.07546,
    "j": 0.00153,
    "k": 0.01292,
    "l": 0.04025,
    "m": 0.02406,
    "n": 0.06749,
    "o": 0.07507,
    "p": 0.01929,
    "q": 0.00095,
    "r": 0.07587,
    "s": 0.06327,
    "t": 0.09356,
    "u": 0.02758,
    "v": 0.00978,
    "w": 0.02560,
    "x": 0.00150,
    "y": 0.01994,
    "z": 0.00077,
}

def decrypt(message):
    chi_test_statistic_values: dict[int, tuple[float, str]] = {} #Shift -> (Test Statistic, Shift) dictionary
    for s in range(len(alphabet)): #Iterate through all possible shifts (0-26 or amount of characters)
        message_shifted = ""
        for c in message: #Iterate through all characters in encrypted string
            if c in alphabet:
                pos = alphabet.find(c) #Original position
                pos_new = (pos - s) % len(alphabet) #Shifted position
                c_new = alphabet[pos_new] #Shifted character
                message_shifted += c_new #Add to shifted string
            else:
                message_shifted += c
        chi_test_statistic = 0.0
        for c in message_shifted: #Iterate through all characters in shift
            if c in frequencies:
                occ = message_shifted.count(c) #Get occurrence of characters in shift
                occ_expected = frequencies[c] * occ #Get expected occurrence from frequencies
                chi_letter_value = ((occ - occ_expected) ** 2) / occ_expected #Get test statistic
                chi_test_statistic += chi_letter_value #Add test statistic to total
        chi_test_statistic_values[s] = ( #Add test statistic value to 
            chi_test_statistic,
            message_shifted
        )
        def sorting_key(key: int) -> tuple[float, str]: #Get key (Don't understand this yet)
            return chi_test_statistic_values[key]
        shift_best_key: int = min( #Find key of lowest test statistic value (Don't understand this yet)
            chi_test_statistic_values,
            key=sorting_key,
        )
        (
            shift_best_test_statistic,
            shift_best,
        ) = chi_test_statistic_values[shift_best_key] #Get data of most correct shift
    print("Shift #" + str(shift_best_key) + ": " + shift_best)

decrypt(input("Enter message to decrypt: ").lower())