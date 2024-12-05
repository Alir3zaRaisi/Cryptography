import random
import math

'''To find e,d values'''
def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    s0, s1, t0, t1 = 1, 0, 0, 1
    if a > b:
        r0, r1 = a, b
    else:
        r1, r0 = a, b
    while(r1 != 0):
        ri = r0 % r1
        qi = r0 // r1
        si = s0 - qi * s1
        ti = t0 - qi * t1
        t0, t1 = t1, ti
        s0, s1 = s1, si
        r0, r1 = r1, ri
    return r0, s0, t0 % a

'''Split string to blocks size of modulus so it can be encrypted/decrypted'''
def split_into_blocks(data, block_size):
    return [data[i:i + block_size] for i in range(0, len(data), block_size)]

'''Convert bytes to ascii to show to result'''
def bytes_to_ascii(data:bytes)-> str:
    bits_in_string = ""
    result = ''
    for x in data:
        bits_in_string+=((bin(x)[2:].rjust(8, '0')))

    for x in range(0, len(bits_in_string), 7):
        my_int = bits_in_string[x:x+7].ljust(7, '0')
        my_int = int(my_int, 2)
        result += chr(my_int)

    return result

'''Convert ascii to bytes so it can be decrypted'''
def ascii_to_bytes(text:str)-> bytes:
    bits_in_string = ''
    for x in text:
        bits_in_string += (bin(ord(x))[2:]).rjust(7, '0') 

    my_bytes = b''
    for x in range(0, len(bits_in_string), 8):
        my_byte = bits_in_string[x:x+8]
        if len(my_byte) == 8:
            my_bytes += int(my_byte, 2).to_bytes(1, 'big')
    return my_bytes

'''RSA Class to encrypt/decrypt data'''
class RSA:
    def __init__(self, modulus: int, public_key: int, private_key: int) -> None:
        self.modulus = modulus
        self.private_key = private_key
        self.public_key = public_key
        max_block_size = math.floor(math.log(modulus, 128))
        self.block_size = max_block_size

    '''gets plain text as input then split it into bytes size of modulus and then encrypt each block'''
    def encrypt(self, plaintext: str) -> str:
        plaintext_bytes = plaintext.encode('utf-8')
        blocks = split_into_blocks(plaintext_bytes, self.block_size)
        encrypted_data = b""
        for block in blocks:
            block_int = int.from_bytes(block, byteorder='big')
            encrypted_int = pow(block_int, self.public_key, self.modulus)
            encrypted_bytes = encrypted_int.to_bytes((encrypted_int.bit_length() + 7) // 8, 'big')
            # Padding to ensure each block is the same size
            encrypted_data += encrypted_bytes.rjust(self.block_size, b'\0')

        return bytes_to_ascii(encrypted_data)

    '''gets ascii text as input then splits into modulus size '''
    def decrypt(self, ciphertext: str) -> str:
        my_bytes = ascii_to_bytes(ciphertext)
        blocks = split_into_blocks(my_bytes, self.block_size)
        decrypted_data = b""

        for block in blocks:
            block_int = int.from_bytes(block, byteorder='big')
            decrypted_int = pow(block_int, self.private_key, self.modulus)
            decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big')
            decrypted_data += decrypted_bytes

        return decrypted_data.decode('utf-8')

'''Genrate Random and test if it prime then generate Public key, Private key and modulus'''
class KeyGenerator:
    def __init__(self, prime_size: int) -> None:
        self.prime_size = prime_size
        self.key_size = 2 * prime_size

    def prime_check(self, number: int, security_parameter: int = 5) -> bool:
        if number % 2 == 0:
            return False

        u, r = 0, number - 1
        while r % 2 == 0:
            r //= 2
            u += 1
        for _ in range(security_parameter):
            a = random.randint(2, number - 2)
            x = pow(a, int(r), number)
            if x != 1 and x != number - 1:
                for _ in range(u - 1):
                    x = pow(x, 2, number)
                    if x == 1:
                        return False
                if x != number - 1:
                    return False
        return True

    def generate_random(self, number_size: int = 512) -> int:
        random_bits = random.getrandbits(number_size)
        return random_bits

    def generate_random_prime(self, prime_size: int = 512):
        random_number = self.generate_random(prime_size)
        cnt = 0
        res = self.prime_check(random_number)
        while res == False:
            cnt += 1
            random_number = self.generate_random()
            res = self.prime_check(random_number)
        print(f"Generated {cnt} Random numbers")
        return random_number

    def generate_keys(self, key_size: int = 512) -> tuple:
        prime1 = self.generate_random_prime(key_size)
        prime2 = self.generate_random_prime(key_size)

        modulus = prime1 * prime2

        phi = (prime1 - 1) * (prime2 - 1)

        gcd = -1
        public_key, private_key = 0, 0
        while gcd != 1:
            public_key = random.randint(3, phi - 1)
            gcd, _, private_key = extended_gcd(phi, public_key)
        return(modulus, public_key, private_key)

