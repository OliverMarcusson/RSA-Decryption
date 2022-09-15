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

def get_keypair(F):
    while True:
        encryption_key = random.randint(1, F)
        if is_prime(encryption_key) == True:
            break
    
    decryption_key = 1
    while True:
        if (decryption_key * encryption_key) % F == 1:
            return encryption_key, decryption_key
        else:
            decryption_key += 1
 
print('What do you want to do?\n1. Encrypt\n2. Decrypt')
option = int(input(':'))

if option == 1:
    print('Do you have an encryption key?\n1. Yes\n2. No')
    has_keypair = int(input(':'))
    
    if has_keypair == 1:
        encryption_key = int(input('\nPlease enter encryption key: '))
    
    message = int(input('Please input a message to encrypt: '))
    prime_numbers = find_primes(100)
    p = prime_numbers[-1]
    q = prime_numbers[-2]
    n = p*q
    F = (p-1)*(q-1)
    
    if has_keypair != 1:
        encryption_key, decryption_key = get_keypair(F)
    
    encrypted_message = (message ** encryption_key) % n
    
    if has_keypair != 1:
        print(f"\nDone!\nEncrypted message: {encrypted_message}\n\n[ Keypair ]\nEncryption:{encryption_key}\nDecryption:{decryption_key}")
    else:
        print(f"\nDone!\nEncrypted message: {encrypted_message}\n\n[ Key ]\nEncryption:{encryption_key}")



elif option == 2: 
    encrypted_message = int(input('Please input a message to decrypt: '))
    decryption_key = int(input('Please input your decryption key: '))
    prime_numbers = find_primes(100)
    p = prime_numbers[-1]
    q = prime_numbers[-2]
    n = p*q
    decrypted_message = (encrypted_message ** decryption_key) % n
    print(f"\nDone!\nDecrypted message: {decrypted_message}\n\n[ Key ]\nDecryption:{decryption_key}")

