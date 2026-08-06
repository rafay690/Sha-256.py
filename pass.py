import hashlib
# Ask the user to enter a password
password = input("Enter Password: ")
# Convert the password into bytes because SHA-256 works with bytes
encoded_password = password.encode()
# Generate the SHA-256 hash and convert it to hexadecimal format
hashed_password = hashlib.sha256(encoded_password).hexdigest()
# Display the hashed password
print("Stored Password Hash:")
print(hashed_password)