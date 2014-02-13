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

def make_chains(n, corpus):

    tokens = tokenize(corpus)

    if len(tokens) < n:
        return

    for i in range(len(tokens) - n):

        gram = tuple(tokens[i:i+n])

        next = tokens[i + n]

        if gram in ngrams:
            ngrams[gram].append(next)
        else:
            ngrams[gram] = [next]

    return ngrams


def make_text(n,ngrams):

    output_string = ""
    counter = 0

    while len(output_string) < 110:

        if counter == 0:

            first_seed = ""

            while not first_seed.istitle():
                current = random.choice(ngrams.keys())

                first_seed, second_seed = current


        else:

            random_word = random.choice(ngrams[current])

            first_word, second_word = current

            current = (second_word, random_word)

            output_string = output_string + " " + random_word

        counter += 1


    if not random_word[-1] in ('.!?'):
        while not random_word[-1] in ('.!?'):
            random_word = random.choice(ngrams[current])
            first_word, second_word = current
            
            current = (second_word, random_word)

        return first_seed + " " + second_seed + output_string + " " + random_word
    else:
        return first_seed + " " + second_seed + output_string

    
    

def main():
    args = sys.argv
    f = open(args[1])


    # Change this to read input_text from a file
    input_text = f.read()
    f.close()

    tweet_text = make_chains(2, input_text)
    print make_text(2, tweet_text)
    # twitter_junk(tweet_text)


      #Twitter Authorization settings for Ron Suess user account
    # api = twitter.Api(consumer_key='dw71KKcWg6fzxozOv5W0Q',consumer_secret='AxoPHUcRDl211E9a0PdpK6dg4ezkEYynZA79ZgO78', access_token_key='1278546524-FaFhodBWscK8KUH85Q4lzxpP4O1T6zaP4WAuY52',access_token_secret='AU0VPtJJQIyASUfirYQ0tNOZLY2UBLjNsBvTbom49Ho')

    # #Send tweet of random_text to twitter account
    # status = api.PostUpdate(random_text)

   

if __name__ == "__main__":
    main()