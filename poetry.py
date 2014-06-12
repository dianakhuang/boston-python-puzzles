import string
import random

poem = '''a narrow fellow in the grass
occasionally rides;
you may have met him, did you not,
his notice sudden is.

the grass divides as with a comb,
a spotted shaft is seen;
and then it closes at your feet
and opens further on.

he likes a boggy acre,
a floor too cool for corn.
yet when a child, and barefoot,
i more than once, at morn,

have passed, i thought, a whip-lash
unbraiding in the sun,
when, stooping to secure it,
it wrinkled, and was gone.

several of nature's people
i know, and they know me;
i feel for them a transport
of cordiality;

but never met this fellow,
attended or alone,
without a tighter breathing,
and zero at the bone.'''

# translation dictionary
rosetta_stone  = {}
reverse_map = {}
invalid = set(['\''])

# construct the dictionary
for char in string.lowercase:
    key = poem.count(char)
    # this means we have a duplicate
    if key in rosetta_stone:
        old_char = rosetta_stone[key] 
        # add the two duplicates to the invalid set so we will not use them
        invalid.add(old_char)
        invalid.add(char)
    rosetta_stone[key] = char
    reverse_map[char] = key

def contains_dupe_char(word):
    for dupe_char in invalid:
        if dupe_char in word:
            return True
    return False

WORD_FILE = '/usr/share/dict/words' 
def generate_word_list():
    """
    Generate a list of words that can be encoded, 
    """
    with open(WORD_FILE) as f:
        words = f.readlines()
        words_no_dupes = [word.lower() for word in words if not contains_dupe_char(word.lower())]
        return words_no_dupes

def encode_word(word):
    encoded = []
    for char in word[:-1]:
        encoded.append(reverse_map[char])
    return encoded

def find_largest(word_list):
    word_lengths = [(word, len(word)) for word in word_list]

    sorted_lengths = sorted(word_lengths, key=lambda x: x[1])

    largest = sorted_lengths[-1][0]
    print largest
    print encode_word(largest)

    
def generate_word():
    word_list = generate_word_list()
    chosen_word = random.choice(word_list)
    generated = encode_word(chosen_word)
    print chosen_word
    print generated

def say(keys):
    """
    Given a list of keys, print the matching characters

    keys: a list of numbers that must be decoded

    """
    final_str = ""
    for key in keys:
        final_str += rosetta_stone[key]
    print final_str

say([56,38,44,56,29])
say([29, 33, 38, 10, 30])
generate_word()
generate_word()

word_list = generate_word_list()
find_largest(word_list)
