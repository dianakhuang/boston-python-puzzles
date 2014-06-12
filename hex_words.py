import string

def to_int(hex_str):
    return int(hex_str, 16)

HEX_CHARS = set(string.lowercase[0:6])
def hex_word(word):
    for c in word.lower():
        if c not in HEX_CHARS:
            return False
    return True

WORD_FILE = '/usr/share/dict/words' 
def generate_word_list():
    """
    Generate a list of words that can be encoded, 
    """
    with open(WORD_FILE) as f:
        words = f.readlines()
        # need to chop off the new lines at the end
        hex_words = [word.lower()[:-1] for word in words if hex_word(word[:-1])]
        return hex_words

def find_largest(word_list):
    word_lengths = [(word, to_int(word)) for word in word_list]
    sorted_lengths = sorted(word_lengths, key=lambda x: x[1])

    largest = sorted_lengths[-1][0]
    print largest

word_list = generate_word_list()
find_largest(word_list)
