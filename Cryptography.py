from cryptography.fernet import Fernet

# Step 1: Generate a secret key
key = Fernet.generate_key()  # This generates a random secret key
cipher_suite = Fernet(key)  # Create a cipher object using the secret key

# Step 2: Encrypt a message
message = "Hello, this is a secret message!"
encoded_message = message.encode()  # Convert the message to bytes
encrypted_message = cipher_suite.encrypt(encoded_message)  # Encrypt the message

# Step 3: Decrypt the encrypted message
decrypted_message = cipher_suite.decrypt(encrypted_message).decode()  # Decrypt and decode the message

# Output
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
