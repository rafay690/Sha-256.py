import hashlib
# Asking user to enter msg
message = input("Enter Message: ")
#Convert the message into bytes because SHA-256 works with bytes
encoded_message = message.encode()
# Generating hash/converting it to hexadecimal format
hash_value = hashlib.sha256(encoded_message).hexdigest()
# display Hash
print("SHA-256 Hash:")
print(hash_value)
