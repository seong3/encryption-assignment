# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
import copy
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        
       # pass #delete this line and replace with your code here
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
        
      #  pass #delete this line and replace with your code here

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return copy.deepcopy(self.valid_words)
     #   pass #delete this line and replace with your code here
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        perm_dict = {}
        
        for i in range(len(VOWELS_LOWER)):
            perm_dict[VOWELS_LOWER[i]] = vowels_permutation[i]
            perm_dict[VOWELS_UPPER[i]] = vowels_permutation[i].upper()
        

        for letters in CONSONANTS_LOWER:
            perm_dict[letters] = letters



        for letters in CONSONANTS_UPPER:
            perm_dict[letters] = letters

        return perm_dict
        
        
        
       # pass #delete this line and replace with your code here
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        text = self.get_message_text()
        
        new_text=""
        
        for letter in text:
            if letter in transpose_dict:
                new_text += transpose_dict[letter]
        
            else:
                new_text += letter
        
        return new_text
        #pass #delete this line and replace with your code here
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self,text)
        
        
       # pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
      
    
        
        # Call list of valid words to check with
        word_list = self.get_valid_words()
        
        #call a list of all permutations of vowels
        list_vowels_permutation = get_permutations(VOWELS_LOWER)
        
        # create a dictonary which uses each permutation as keys and the amount of valid words as value
        correct_words = {}
        
        #For each permutation in the list
        for vowel_permutation in list_vowels_permutation:
            
            #Add permutation to our correct_words dictionary
            correct_words[vowel_permutation] = 0

            # Make a transpose dictionary
            transpose_dict = self.build_transpose_dict(vowel_permutation)
                
            # apply the encryption/transformation to get a new word
            new_text = self.apply_transpose(transpose_dict)
            
            # create a list with each word in sentence being an element
            new_text_list = new_text.split()
                
            # Now for each word in our text list
            for word in new_text_list:
                
                # Check if our new word is a valid word
                if is_word(word_list, word) == True:
                    
                    # and if correct add 1 to the value of the permutation in the dictionary
                    correct_words[vowel_permutation] += 1
                   # print correct_words
                
        
        # Find permutation with the most correct words
        best_permutation = max(correct_words, key=correct_words.get)
        
        # IF there exists a permutation with more than 1 correct word
        if best_permutation > 0:
            
            # build our transpose dictionary
            best_transpose_dict = self.build_transpose_dict(best_permutation)
            
            #decrypr the text
            decrypted_text = self.apply_transpose(best_transpose_dict)
            
            return decrypted_text
        
        #if all permutations have 0 correct words return original message
        else:
            return self.get_message_text()
        
        
        pass #delete this line and replace with your code here
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    #print("Original message:", message.get_message_text(), "Permutation:", permutation)
    #print("Expected encryption:", "Hallu Wurld!")
    #print("Actual encryption:", message.apply_transpose(enc_dict))
   # enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
   # print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    
    c = EncryptedSubMessage("Hallu this is tha king spaeking sop")
    print c.decrypt_message()
    