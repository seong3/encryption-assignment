# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
import copy

lower = string.ascii_lowercase
upper = string.ascii_uppercase


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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        pass #delete this line and replace with your code here

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.text
        pass #delete this line and replace with your code here

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return copy.deepcopy(self.valid_words)
        pass #delete this line and replace with your code here

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        cipher_dict = {}

        # shift each letter in lower down a certain number of places
        for letter in lower:
            cipher_dict[letter] = lower[(lower.index(letter) + shift) % 26]
        
        # shift each letter in upper down a certain number of places
        for letter in upper:
            cipher_dict[letter] = upper[(upper.index(letter) + shift) % 26]

        return cipher_dict
        
      #  pass #delete this line and replace with your code here

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        # call our text
        text = self.get_message_text()
        
        # build our dictionary with the shift value
        cipher_dict = self.build_shift_dict(shift)
        
        #create an empty string which we will later add to
        new_text=""
        
        # for each letter in our text we
        for letter in text:
            #check if it is in our cypher dictionary
            if letter in cipher_dict:
                #and if it is we convert it to its new value and add it to our string new_text
                new_text += cipher_dict[letter]
            
            # if not in cypher dictionary we leave it as it is
            else:
                new_text += letter
        
        return new_text
                
        #pass #delete this line and replace with your code here

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self,text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
        #pass #delete this line and replace with your code here

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift
#        pass #delete this line and replace with your code here

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        
        return copy.deepcopy(self.encryption_dict)
       # pass #delete this line and replace with your code here

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''

        return self.message_text_encrypted
       # pass #delete this line and replace with your code here

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
        #pass #delete this line and replace with your code here


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)
        #pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        # import word list to have a list of valid wordsa
        word_list = self.get_valid_words()
        
        
        real_words ={} # dictionary with key: being the amount shifted by and value: the number of valid words after shift

        # go through every shift      
        for i in range(26): 
            
            # add the shift to the dictionary
            real_words[i] = 0       

            # shift our text with our new shift value i   
            new_text = self.apply_shift(i)
            
            # turn this new text into a list with each word being an element
            list_new_text = new_text.split()
            
            # then check how many of the words in this list are valid
            for word in list_new_text:
                if is_word(word_list, word) == True:
                    
                    # and add this value to the dictionary real_words
                    real_words[i] += 1
        
        # find the shift with the most valid words
        shift = max(real_words, key=real_words.get)
        
        #shift our text by this number
        text = self.apply_shift(shift)
        
        
        return(shift, text)
        
        pass #delete this line and replace with your code here
if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
   # plaintext = PlaintextMessage('hello', 2)
    #print('Expected Output: jgnnq')
    #print('Actual Output:', plaintext.get_message_text_encrypted())
    #plaintext.change_shift(3)
    #print plaintext.get_message_text_encrypted()

#
#    #Example test case (CiphertextMessage)
   # ciphertext = CiphertextMessage("jgnnq")
   # print('Expected Output:', (24, 'hello'))
   # print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    story = "Xoqy Tzcfsm wg o amhvwqoz qvofoqhsf qfsohsr cb hvs gdif ct o acasbh hc vszd qcjsf ob wbgittwqwsbhzm dzobbsr voqy. Vs vog pssb fsuwghsfsr tcf qzoggsg oh AWH hkwqs pstcfs, pih vog fsdcfhsrzm bsjsf doggsr oqzogg. Wh vog pssb hvs hforwhwcb ct hvs fsgwrsbhg ct Sogh Qoadig hc psqcas Xoqy Tzcfsm tcf o tsk bwuvhg soqv msof hc sriqohs wbqcawbu ghirsbhg wb hvs komg, asobg, obr shvwqg ct voqywbu."
    ciphertext = CiphertextMessage(story)
    print ciphertext.decrypt_message()    
    pass #delete this line and replace with your code here
