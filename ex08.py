#!/usr/bin/env python
import random
import sys


def make_chains(fileObject):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dict = {}

    count = 0
    
    content = fileObject.read()
    noSpaceInFile = content.split()


    for i in noSpaceInFile:
        if count < len(noSpaceInFile)-2:
            word_tuple = noSpaceInFile[count], noSpaceInFile[count + 1]
        
            if word_tuple not in markov_dict:
                markov_dict[word_tuple] = [noSpaceInFile[count + 2]]
            else:
                markov_dict[word_tuple].append(noSpaceInFile[count + 2])   
            # print "Word tuple: %r and Word Value: %r" % (word_tuple, word_value)
            count+= 1

    return markov_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    for keys in chains:
        temp_key = random.choice(keys)
        if temp_key not in chains[key]:
            temp_value = chains[temp_key]
    print temp_key, temp_value

    #choose random key
    #choose random value from [key]value
    #print result of above
    #append new key and new value into dictionary


    # for keys in chains:
    #     #print the key, then print the sampled values
    #     print keys, random.choice(chains[keys])





def main():
    fileObject = open(sys.argv[1])
    chain_dict = make_chains(fileObject)
    return make_text(chain_dict)

    # Change this to read input_text from a file
    #input_text = "Some text"

    
    #random_text = make_text(chain_dict)
    
    #print random_text

if __name__ == "__main__":
    main()