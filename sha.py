import hashlib
# Asking user to enter msg
message = input("Enter Message: ")
# converts text to byte for sha256 as it only take bytes
encoded_message = message.encode()
# Generating hash/converting it to hexadecimal strig
hash_value = hashlib.sha256(encoded_message).hexdigest()
# hash printing
print("SHA-256 Hash:")
print(hash_value)