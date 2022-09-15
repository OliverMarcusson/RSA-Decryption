import random

def find_primes(amount):
    prime_numbers = []
    for number in range(amount):
        prime = True
        for i in range(number):
            if not i == number and not i == 1 and not i == 0 and not number == 0:
                if number % i == 0:
                    prime = False
        
        if prime == True:
            prime_numbers.append(number)
            
    return prime_numbers

def is_prime(number):
    prime = True
    for i in range(number):
            if not i == number and not i == 1 and not i == 0 and not number == 0:
                if number % i == 0:
                    prime = False

    if prime == True:
        return True
    else:
        return False

def find_enc():
    while True:
        encryption_key = random.randint(1, F)
        if is_prime(encryption_key) == True:
            return encryption_key

def find_decryption(encryption_key):
    i = 1
    while True:
        if (i * encryption_key) % F == 1:
            return i
        else:
            i += 1

def main():
       
    prime_numbers = find_primes(100)
    p = prime_numbers[-1]
    q = prime_numbers[-2]
    n = p*q
    F = (p-1)*(q-1)

    

    print(f"p: {p}\nq: {q}\nn: {n}\nF: {F}\nENC key: {encryption_key}")


    decryption_key = find_decryption()

    message = 69
    decrypted = (encrypted ** decryption_key) % n

    print(f"\nOriginal Message: {message}")
    print(f"Encrypted message: {encrypted}")
    print(f"Decrypted message: {decrypted}")
 
print('What do you want to do?\n1. Encrypt\n2. Decrypt')
option = int(input(':'))

if option == 1:
    message = int(input('Please input a message to encrypt:'))
    prime_numbers = find_primes(100)
    p = prime_numbers[-1]
    q = prime_numbers[-2]
    n = p*q
    F = (p-1)*(q-1)
    encryption_key = find_enc()
    encrypted = (message ** encryption_key) % n
    
    print(f"Done!\nEncrypted message: {encrypted}\nEncryption key: {encryption_key}")



else: 
    encrypted_message = int(input('Please input a message to decrypt:'))

