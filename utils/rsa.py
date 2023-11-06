import random

# this function makes it easier to calculate large numbers (exponentiation by squaring)
def modBig(num, pow, mod):
    result = 1 # Initialize the result to 1
    num = num % mod # Reduce num modulo mod to ensure it's within bounds

    while pow > 0: 
        if pow % 2 == 1:  # If pow is odd
            result = (result * num) % mod  # Multiply result by num and take modulo mod
        
        pow = pow >> 1  # Right-shift pow by 1 (equivalent to integer division by 2)
        num = (num * num) % mod  # Square num and take modulo mod

    return result  # Return the final result


# rsa encryption implementation
def encrypt(message, n, e, block_size = 2):
    encrypted_blocks = []
    ciphertext = -1

    if (len(message) > 0):
        # initialize ciphertext to the ASCII of the first character of message
        ciphertext = ord(message[0])

    for i in range(1, len(message)):
        if (i % block_size == 0): # when ciphertext size reaches block_size
            encrypted_blocks.append(ciphertext)
            ciphertext = 0 # reset ciphertext buffer

        # multiply by 1000 to shift the digits over to the left by 3 places since ASCII codes are a max of 3 digits in decimal; then add the ASCII code of the current character (xxx -> xxx000 + yyy = xxxyyy)
        ciphertext = ciphertext * 1000 + ord(message[i])

    # add the last block to the list
    encrypted_blocks.append(ciphertext)

    # encrypt each block individually
    for i in range(len(encrypted_blocks)):
        encrypted_blocks[i] = str(modBig(encrypted_blocks[i], e, n))

    # create a string from the numbers
    encrypted_message = " ".join(encrypted_blocks)
    
    return encrypted_message


def decrypt(blocks, n, d, block_size = 2):
    # turns the string into a list of ints
    list_blocks = blocks.split(' ')
    int_blocks = []

    for s in list_blocks:
        int_blocks.append(int(s)) # get each block

    message = ""

    # converts each int in the list to block_size number of characters
    for i in range(len(int_blocks)):
        # decrypt all of the numbers by taking it to the power of d
        # and modding it by n
        int_blocks[i] = modBig(int_blocks[i], d, n)
        
        tmp = ""
        # take apart each block into its ASCII codes for each character
        # and store it in the message string
        for c in range(block_size):
            tmp = chr(int_blocks[i] % 1000) + tmp
            int_blocks[i] //= 1000
        message += tmp

    return message


# Function to calculate convergents from the continued fraction.
def convergents(cf):
    convs = []
    num1, num2 = 1, 0  # initial numerators
    den1, den2 = 0, 1  # initial denominators

    for x in cf:
        # The new numerator and denominator are calculated based on the previous two convergents.
        a = x * num1 + num2
        b = x * den1 + den2

        # Update the last two numerators and denominators
        num2, num1 = num1, a
        den2, den1 = den1, b

        convs.append((a, b))

    return convs



def wiener_atk(e, n, original_d):
    ops = 0 # number of operations
    potential_d = [] # List to store potential private keys
    cf = []  # List to store the continued fraction representation.
    
    # Calculate the continued fraction representation. 
    while n != 0:
        cf.append(e // n)
        e, n = n, e % n
        ops += 1
        
    
    convergent_list = convergents(cf)
    ops += len(cf)

    # For each convergent   
    for (k, d) in convergent_list:
        if k == 0 or d % 2 == 0: # If k is 0 or d is even,
            continue

        if d == original_d:
                print("Decrypted, attack worked!")

        potential_d.append(d)
        ops += 1
    ops += len(convergent_list)

    return potential_d, ops


def check_private_key(potential_d, e, n):
    # get random integer
    M = random.randint(1, 1000)
    correct_d = -1
    for d in potential_d:
        if modBig(modBig(M, e, n), d, n) == M: # this is equivalent to M^ed mod n == M, since ed = 1 mod phi(n)
            correct_d = d
            break
    if correct_d == -1:
        print("Could not find correct private key")
    return correct_d