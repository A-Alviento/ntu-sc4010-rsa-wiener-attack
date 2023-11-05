import random
import time

# generate unique random numbers
def gen_unique_random_numbers(count, range_start, range_end):
    unique_numbers = set()
    while len(unique_numbers) < count:
        unique_numbers.add(random.randint(range_start, range_end))
    return list(unique_numbers)


# one pass of miller rabin test
def miller_rabin(p_candidate, s):
    '''
    p_candidate - 1 = 2^u * r 
    s is the security parameter, i.e. the number of iterations
    '''
    start_time = time.time() # start timer

    if p_candidate < s+3:
        raise ValueError("p_candidate must be greater than s")
    
    # get s random numbers, a in [2, p_candidate - 2]
    a = []
    # generate s unique random numbers from [2, p_candidate - 2]
    a = gen_unique_random_numbers(s, 2, p_candidate - 2)

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
                end_time = time.time()
                return False, end_time-start_time # composite
    
    end_time = time.time()
    return True, end_time-start_time # likely prime


# generate a prime number of nbits bits
def gen_prime(nbits, s):
    '''
    nbits - number of bits of the prime number
    s - number of iterations of the miller rabin test
    '''
    while True:
        p_candidate = random.getrandbits(nbits) # generate a random number of nbits bits

        # force p_candidate to have nbits and be odd
        p_candidate |= 2**nbits | 1 # this is equivalent to p_candidate = p_candidate | 2**nbits | 1 where | is the bitwise OR operator

        if miller_rabin(p_candidate, s):
            return p_candidate


# generate a prime number in the range [start, stop]
def gen_prime_range(start, stop, s):
    while True:
        p_candidate = random.randint(start, stop) # generate a random number in the range [start, stop]

        # force p_candidate to be odd
        p_candidate |= 1 # this is equivalent to p_candidate = p_candidate | 1 where | is the bitwise OR operator

        if miller_rabin(p_candidate, s):
            return p_candidate
        

# generate a prime pair (p, q) such that p < q < 2p
def getPrimePair(nbits, s):
    p = gen_prime(nbits, s)
    q = gen_prime_range(p+1, 2*p, s)

    return p, q


# gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# generate keys 
def gen_vulnerable_keys(nbits, s):
    p, q = getPrimePair(nbits//2, s)
    n = p * q # calculate rsa modulus
    phi = (p-1) * (q-1) # calculent totient of n

    # generate d such that d is coprime to phi and 36d^4 < n
    flag = False
    while not flag:
        d = random.getrandbits(nbits//4) # generate a random number with 1/4th the bit length of n
        if (gcd(d, phi) == 1 and 36 * pow(d, 4) < n):
            flag = True
    
    e = pow(d, -1, phi) # calculate the public exponent e as the modular inverse of d modulo phi(n)

    return e, n, d



