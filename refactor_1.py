from timeit import default_timer

def bin_exp_mod(a, n, b):
    """
    >>> bin_exp_mod(3, 4, 5)
    1
    >>> bin_exp_mod(7, 13, 10)
    7
    """
    #! mod b
    assert not (b==0), "This cannot accept module that is == 0"
    if n == 0:
       return 1
   
    if n % 2 == 1: 
        return (bin_exp_mod(a, n -1, b)* a) % b
    
    r = bin_exp_mod(a, n / 2, b)
    return (r * r) % b

start = default_timer()
bin_exp_mod(7, 13, 10)
finish = default_timer()
print(finish - start)