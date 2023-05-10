def fast_exp(b, e, m):
    init = 2
    powers = [b]
    while init <= e:
        powers.append((powers[-1]**2) % m)
        init *= 2
    binary = bin(e)[2:][::-1]
    product = 1
    for i in range(len(binary)):
        if binary[i] == '1':
            product *= powers[i]
            product %= m
    return product

def char_to_int(char):
    return ord(char) - 96

def int_to_char(num):
    return chr(num + 96)

p, g, a, G_b = 31, 3, 17, 23

pub_key = fast_exp(g, a, p)
print(f"public key = {pub_key}")
pri_key = fast_exp(G_b, a, p)
inv_pri_key = fast_exp(pri_key, p - 2, p)
print(f"private key = {pri_key}")
print(f"private key inverse = {inv_pri_key}")
message = "campus"
encrypted = []
for letter in message:
    encrypted.append(char_to_int(letter) * pri_key % p)
print(f"Encrypted message: {encrypted}")
decrypted = [15,29,26,27,1,20,26]
decrypted_message = ""
for num in decrypted:
    decrypted_message += int_to_char(num * inv_pri_key % p)
print(f"Decrypted message: {decrypted_message}")