"""Generate Markov text from text files."""

from random import choice


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
    print(chains)

    #         for tupled_items in words:
    #             # value_add = words[tupled_items[index]]
    #     value_list.append(value_add)
    #     chains[tupled_items] = value_list        
    #     # tupled_items = (words[index], words[index + 1])
    
    #         #chains[tupled_items] = value_list

    #     # if words[index] != words[-2]:
    #     #     for pair in tupled_items:
    #     #         value_add = [words[index + 2]]
    #     #         value_list.append(value_add)
    #     #     chains[tupled_items] = value_list
    #     # else:
    #     #     pass
    # #value_list = []   
    # # for  tuples in tupled_items:
    # #     value_list.append(tupled_items[index])

    # chains[tupled_items] = value_list
    # print(chains.items())
    # # your code goes here

    # #return chains
make_chains(open_and_read_file("green-eggs.txt"))


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
