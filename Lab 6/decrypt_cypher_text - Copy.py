# def decrypt_cypher_text(encrypted_text, key):
#     # function implementation here...

def decrypt_cypher_text(text, key):
    decrypted_text = ""
    for char in text:
        ascii_code = ord(char)
        new_ascii_code = ascii_code - key
        new_ascii_code = new_ascii_code % 256
        decrypted_text += chr(new_ascii_code)
    return decrypted_text


encrypted_text = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#eh#d#ehwwhu#ghyhorshu$"
key = 3
decrypted_text = decrypt_cypher_text(encrypted_text, key)
print(decrypted_text)