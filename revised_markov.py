#!/usr/bin/env python

import sys
import random
import twitter
import authenticate




ngrams = dict()
max_num = 10

beginnings = []

def twitter_junk(random_text):
    api = twitter.Api(consumer_key=authenticate.api_key,
                      consumer_secret=authenticate.api_secret,
                      access_token_key=authenticate.access_token,
                      access_token_secret=authenticate.access_token_secret)
    api.PostUpdate(random_text)

def tokenize(corpus):
    return corpus.split()

def feed(corpus, n):

    tokens = tokenize(corpus)

    if len(tokens) < n:
        return

    # store the first ngram of this line
    # tokens[:n] says 'get all the tokens until we reach n'
    # then, cast that list as a tuple, and append it to the list called beginnings.
    # we cast the list as a tuple in order for it to be a key. keys must be immutable.
    # we then append the tuple because it is a single value

    beginning_rseed = random.randint(0,len(tokens))

    beginning = tuple(tokens[beginning_rseed:(beginning_rseed + n)])
    # if not tokens[beginning_rseed].istitle():
    #     tokens[beginning_rseed].

    beginnings.append(beginning)


    # imagine if we had 10 words and were looking at bi-grams
    # 10 words - 2 = 8. the length is 8. i.e. 
    # the length would be: 
    #   0,   1,   2,   3,   4,   5,   6,   7, the first eight words. 
   
    for i in range(len(tokens) - n):

        gram = tuple(tokens[i:i+n])

        # example: if i = 1 and we're looking at bigrams
        # then the gram = tuple(tokens[1:3]), which gives us (tokens[1],tokens[2])

        # now, we also have to keep track of the word that comes after whatever
        # the second value in the tuple is.

        # if i = 1, and we're looking at bi-grams, then i + n = 3
        # meaning, tokens[3] 
        # this can be generalized as:

        next = tokens[i + n]

      # the next part is familiar:
      # gram is the key of a two-word pairing, just think of it as one thing.
      # if we've already seen these this before, that means there is
      # already an entry for them in the dictionary. 
      # we append the value of whatever 'next' is to the value list that already
      # exists for this key.

      # otherwise, if we haven't seen this pairing before,
      # we create a new key, value pair. set the new key's value to be a
      # a new list that contains whatever the value of 'next' is

        if gram in ngrams:
            ngrams[gram].append(next)
        else:
            ngrams[gram] = [next]


 
    current = random.choice(beginnings)
    print "beginning current is :", current
    output = list(current)

    # if current is laready in ngrams dictionary, assign its value to 
    # 'possible next.' the values in the dictionary are a list,
    # so regardless of however many items are in the values list, the
    # list is assigned to possible_next

    # then, we select a value from the possible_next list and assign it
    # to the variable 'next.'
    # output is the list-ified version of 'current,' the first bi-gram
    # selected to kick off the markov-chained text. that is why we can 
    # append it.

    for i in range(max_num-1):
        # at the beginning of the program, we set a maximum number of times
        # that we can iterate through the text

        # at this point, we have a beginning tuple and a current one
        # now we have to account for which words MIGHT go next and then 
        # choose randomly from that list of possibilities what WILL go next

        possible_next = []
        if current in ngrams:

            # remember current is a new key selected from the first tuple of
            # two words (assuming we're talking bi-grams)
            print "current is : ", current, "\n"

            # possible_next = the list of all possible words that could follow that key
            # (word pairing, tuple, etc.)

            possible_next = ngrams[current]
            print "possible next is: ", possible_next, "\n"

            # select one of those possibilities and store it in 'next'
            next = random.choice(possible_next)
            print "definite next is: ", next, "\n"

            # append next to output, which is 'current' turned into a list.
            output.append(next)
            print "This makes the output: ", output, "\n"
            
            # so you have:
            # ('word', 'word') + 'new word'

            # here is where things get weird: we have to grab the second word
            # from the current tuple and make a new key with that word and the 
            # 'next'

            # ex. we have "dog cat mouse" and now we want "cat mouse"
            # in other words, get the last n items from the list output

            # cast this word pair as a tuple, so that it can be a new key
            # and assign it as the new value of current.

            current = tuple(output[-n:])
            print "The end of the last output is now assigned to the current value ", current, "\n"

        else:
            break
    
    

    new_end_word = output[-1]
    while not new_end_word[-1] in ('.!?'):
    #find another word that ends with one
       new_end_word = random.choice(tokens)
   

    return ' '.join(output) + ' ' + new_end_word + '\n'

    
    

def main():
    args = sys.argv
    f = open(args[1])


    # Change this to read input_text from a file
    input_text = f.read()
    f.close()

    tweet_text = feed(input_text, 2)
    print tweet_text
    twitter_junk(tweet_text)


      #Twitter Authorization settings for Ron Suess user account
    # api = twitter.Api(consumer_key='dw71KKcWg6fzxozOv5W0Q',consumer_secret='AxoPHUcRDl211E9a0PdpK6dg4ezkEYynZA79ZgO78', access_token_key='1278546524-FaFhodBWscK8KUH85Q4lzxpP4O1T6zaP4WAuY52',access_token_secret='AU0VPtJJQIyASUfirYQ0tNOZLY2UBLjNsBvTbom49Ho')

    # #Send tweet of random_text to twitter account
    # status = api.PostUpdate(random_text)

   

if __name__ == "__main__":
    main()