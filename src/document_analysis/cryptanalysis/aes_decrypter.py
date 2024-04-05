from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_aes(encrypted_text: str, key: bytes) -> str:
    """
    Decrypts an AES encrypted text using the given key.

    Args:
    - encrypted_text: The encrypted text as a base64 encoded string.
    - key: The secret key to use for decryption.

    Returns:
    The decrypted text as a string.
    """
    encrypted_text = b64decode(encrypted_text)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(encrypted_text)
    return unpad(decrypted_text, AES.block_size).decode()

# Example usage
key = b'0123456789abcdef'
encrypted_text = b'U2FsdGVkX186MTIyMzY3Nzc5PQ0KQ29tbWVudDoxMjM0NTY3ODkw'
decrypted_text = decrypt_aes(encrypted_text, key)
print(decrypted_text)