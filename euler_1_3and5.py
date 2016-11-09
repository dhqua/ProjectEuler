'''
Find the sum of all natural numbers that are multiples of 3 and 5
Below the given max num
'''

def sum_mult_3_5(max_num):
    sum = 0
    for num in range(1,max_num):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum
            
            
def test_sum_mult_3_5():
    # Testing the given case, of the max num being 10 and result being 23
    assert sum_mult_3_5(10) == 23

test_sum_mult_3_5()
sum_mult_3_5(1000)
    
