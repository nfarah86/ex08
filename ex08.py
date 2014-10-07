#!/usr/bin/env python

import sys


def make_chains(fileObject):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dict = {}
    markov_key_tuple = ()

    count = 0
    for line in fileObject:
        noSpaceInFile=line.strip().split()
        #print noSpaceInFile


    for i in noSpaceInFile:
        if count < len(noSpaceInFile)-1:
            print noSpaceInFile[count], noSpaceInFile[count + 1]
            count += 1


    # for count in range(len(noSpaceInFile)):
    #     print noSpaceInFile[count - 1], noSpaceInFile[count]
    #     count +=1



    #for i in (len(noSpaceInFile)):
        #go through the list of words, add words phrases to a tuple
        #keep the 2 part of the tuple, move 1 forward, append the next word
        #



        #find the words that follow the binary word
        #we want to get the word, and add that to a dictionary.







    return {}









def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."




def main():
    fileObject = open(sys.argv[1])
    chain_dict = make_chains(fileObject)

    # Change this to read input_text from a file
    #input_text = "Some text"

    
    #random_text = make_text(chain_dict)
    
    #print random_text

if __name__ == "__main__":
    main()