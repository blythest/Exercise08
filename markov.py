#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    n = 2
    wordlist = corpus.split()
    worddict = {}  
    for i in range(len(wordlist)-2):
        x, y = "",""
        (x, y) = wordlist[i:i+n]
        keys = x,y

        if worddict.get(keys):
            worddict[keys].append(wordlist[i+2])
        else:
            worddict[keys] = [wordlist[i+2]]

    return worddict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    #TODO: Start with a capital letter
    #TODO: End with a punctuation (!?.)
    
    upper_bound = 10
    lower_bound = 2
    string = ""
    for i in range(lower_bound, upper_bound + 1):
        if i == 2:
            random_key = random.choice(chains.keys())
        else:
        # select the following word
            random_word = random.choice(chains[random_key])
            x, y = random_key
            # print x, y, random_word
            random_key = (y, random_word)
            string = string + " "+random_word
    return string 
    # for key, value in chains.iteritems():
    #     print random.choice(chains.keys())
    

    # return "Here's some random text."

def main():
    args = sys.argv
    f = open(args[1])


    # Change this to read input_text from a file
    input_text = f.read()
    f.close()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()