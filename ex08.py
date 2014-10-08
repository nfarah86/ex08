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
    new_text = []
    temp_key = random.choice(chains.keys())
    new_text.append(temp_key[0])
    new_text.append(temp_key[1])  
 #   new_text.append(temp_key_initial)



    #print "Here is the temp key: %s, %s" % temp_key
    #print chains[temp_key]


    while temp_key in chains:
        new_value = random.choice(chains[temp_key])
        stringkey= " ".join(temp_key)
        new_text.append(new_value)
        #new_text.append(stringkey + " " +new_value)
        temp_key = temp_key[1], new_value

        for char in temp_key[1]: #we didn't explicitly state that the
        # charecter is looking for a punctuation mark, we were using == 
        #instead of using "in"
            if char in ["?", "!", "."]:
                temp_key = ("000", "000")

    print " ".join(new_text)




def main():
    fileObject = open(sys.argv[1])
    chain_dict = make_chains(fileObject)
    make_text(chain_dict)


if __name__ == "__main__":
    main()