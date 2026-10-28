def fill_in_letters(c_text, p_text, letter_mapping):
    for i in range(len(p_text)):
        c_letter = c_text[i]
        if c_letter not in letter_mapping:
            continue

        map_value = letter_mapping[c_letter]
        if p_text[i] == 'x' and map_value is not -1:
            p_text = p_text[:i] + p_text[i].replace('x', map_value) + p_text[i + 1:]

    return p_text

def get_remaining_words():
    remaining_words = []
    word = ""
    for letter in plaintext:
        if letter in ['{', '}', '-']:
            if 'x' in word:
                remaining_words.append(word)
            word = ""
            continue

        word += letter

    return remaining_words

if __name__ == "__main__":
    ciphertext = "qnb{vsi-fihczlnb-dlyi-vsi-fibv-plaahib-fi-zv-l-hzici-plaahi-mr-l-frtbbihb-plaahi}"
    plaintext = "xxx{xxx-xxxxxxxx-xxxx-xxx-xxxx-xxxxxxx-xx-xx-x-xxxxx-xxxxxx-xx-x-xxxxxxxx-xxxxxx}"

    mapping = {
    'a': -1, 'b': 's', 'c': -1, 'd': -1, 'e': -1, 'f': -1, 'g': -1, 'h': -1, 'i': -1, 'j': -1,
    'k': -1, 'l': -1, 'm': -1, 'n': 'n', 'o': -1, 'p': -1, 'q': 'c', 'r': -1, 's': -1,
    't': -1, 'u': -1, 'v': -1, 'w': -1, 'x': -1, 'y': -1, 'z': -1
    }

    letter_frequency = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
        'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0,
        't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }

    for letter in ciphertext:
        if letter in letter_frequency:
            letter_frequency[letter] += 1

    # loop until no more 'x' in plaintext
    #   try letter-letter pair based on frequency (first try most likely, then 2nd most likely,...)
    #   fill in letters
    #   get remaining words
    #   check if existing letters are possible by matching against dictionary/wordlist
    plaintext = fill_in_letters(ciphertext, plaintext, mapping)
    words_to_match = get_remaining_words()

    with open("wordlist.txt") as wordlist:
        # for word in wordlist:
        #     pass
        pass

        #


