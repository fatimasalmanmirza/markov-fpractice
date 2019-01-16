"""Generate Markov text from text files."""

import random 


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    open_file = open(file_path)
    return open_file.read()
open_and_read_file("green-eggs.txt")

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    
    # text_string = text_string.replace("\n", " ")
    words = text_string.split()
    chains = {}

    # value_list = []
    # index = 0
    for index in range(len(words)-2):

        # if words[index] != words[-2]:
        tupled_items = (words[index], words[index + 1])
        value_items = [words[index + 2]]
        if tupled_items not in chains:
            chains[tupled_items] = value_items
        else:
            chains[tupled_items] = chains[tupled_items] + value_items
    return chains

make_chains(open_and_read_file("green-eggs.txt"))


def make_text(chains):
    """Return text from chains."""
    # tuple index 1 is a new key
    # random item from the value list is the value
    # add tuple key word and random item word to list, join list
    
    
   #print(chains)
    words = []
    new_chains = {}

    
    for key_pair, value_lists in chains.items():
        new_chains[key_pair[1]] = random.choice(value_lists)
    for keys, value_items in new_chains.items():
        if keys not in words:
            words.append(keys)
            words.append(value_items)
    
   
    print(" ".join(words))


input_path = "green-eggs.txt"
make_text(make_chains(open_and_read_file("green-eggs.txt")))
# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
