import random

# one pass of miller rabin test
def miller_rabin(p_candidate, s):
    '''
    p_candidate - 1 = 2^u * r 
    s is the security parameter, i.e. the number of iterations
    '''
    if p_candidate < s:
        raise ValueError("p_candidate must be greater than s")
    
    # get s random numbers, a in [2, p_candidate - 2]
    a = []
    for i in range(s):
        a_tmp = random.randint(2, p_candidate - 2)
        while a_tmp in a:
            a_tmp = random.randint(2, p_candidate - 2)
        a.append(a_tmp)

    # compute r such that p_candidate - 1 = 2^u * r, with r odd
    r = p_candidate - 1
    u = 0
    while r % 2 == 0:
        r >>= 1 # this is equivalent to r = r // 2
        u += 1 # u is the number of times we can divide r by 2
    

    for i in range(s): # do s primality tests
        z = pow(a[i], r, p_candidate) # z = a^r (mod p)

        if z != 1 and z != p_candidate - 1:  # a^r is not congruent to 1 or -1 (mod p)

            for j in range(1, u): # then we check for all 2r, 4r, 8r, ..., 2^(u-1)r
                z = pow(z, 2, p_candidate) # z = a^(2^j * r) (mod p)
                if z == p_candidate-1: # z = -1 (mod p)
                    break # fails composite test
                
            if z != p_candidate - 1: # means we didn't break out of the loop and thus no -1 was found
                return False # composite

    return True # likely prime