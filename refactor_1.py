from timeit import default_timer

def bin_exp_mod(a, n, b):
    """
    >>> bin_exp_mod(3, 4, 5)
    1
    >>> bin_exp_mod(7, 13, 10)
    7
    """
    #! mod b
    assert not (b==0), "This cannot accept module that is == 0" #* O(1)
    if n == 0: #* O(1)
       return 1 #* O(1)
   
    if n % 2 == 1: #* O(n) * O(1)
        return (bin_exp_mod(a, n -1, b)* a) % b #* O(n)
    
    r = bin_exp_mod(a, n / 2, b) #* O(1)
    return (r * r) % b #* O(n)

    #! Algorithm, point 1: Time complexity = O(n)
    #! Algorithm, point 2: No need for refactor

start = default_timer()
print(bin_exp_mod(3, 4, 5))
print(bin_exp_mod(7, 13, 10))
finish = default_timer()
print(finish - start)