#!/usr/bin/env python

import sys


def make_chains(fileObject):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    
    for line in fileObject:
        noSpaceInFile=line.strip().split()
        print noSpaceInFile





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