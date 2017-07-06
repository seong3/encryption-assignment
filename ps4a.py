# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    # if our string only has one letter the permutation is just itself
    if len(sequence) == 1:
        return sequence
        
    else:
        #create an empty list which we will later store our permutations in
        list1 =[]

        # we first loop through the string picking out a certain element at a time
        for i in range(len(sequence)):
            
            # we ignore the ith character and find the permutations of the rest which will be returned as a list
            lesser_perm = (get_permutations(sequence[0:i] + sequence[i + 1:]))
            
            # then for each element in this list
            for j in range(len(lesser_perm)):
                
                #we add the ith character to the front of this element
                list1.append(sequence[i] + lesser_perm[j])
        return list1

    pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

