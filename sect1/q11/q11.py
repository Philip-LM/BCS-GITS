def xor_encrypt_decrypt(data, key): 
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)]) 
key = b'xdfyg_phi' 
payload = b'\x1a\x05\x15\x11GB\x19HW^DI\x1d\x02\x19_\x1c\n\x08KWII_^XGIK^I__PXW^U' 
decrypted_payload = xor_encrypt_decrypt(payload, key) 
print(f' Decrypted payload: {decrypted_payload}')

print(list(enumerate(payload)))