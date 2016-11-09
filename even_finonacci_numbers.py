import os

'''
By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
'''

def sum_even_fib(max_val):
    #initialize sum to 2 because 2 to account for intial values 
    sum = 2

    #initial 3 terms of sequence
    a = 1
    b = 2
    c = 3

    while( c <= max_val):
        c = a + b

        #adds to sum if current term is even
        if c % 2 == 0:
            sum += c
        print(sum)
        #shifts previos terms before next iteration of the loop
        a = b
        b = c

    #print(sum)
    return sum
    
    
    

def test_sum_even_fib():
    # Test cases for the fib sequence function
    pass
    # assert sum_even_fib(89) == 44 #beginning of sequence given

test_sum_even_fib()

sum_even_fib(89)

os.system('pause')
