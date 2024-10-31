import hashlib

# Input data
data = "Johannes"

# Create a SHA-256 hash object
hash_object = hashlib.sha256()

# Update the hash object with the data (needs to be encoded to bytes)
hash_object.update(data.encode('utf-8'))

# Get the hexadecimal representation of the hash
hash_value = hash_object.hexdigest()

print(f"SHA-256 hash of '{data}': {hash_value}")