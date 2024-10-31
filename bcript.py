import bcrypt

# Hashing a password
password = b"mysecretpassword"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print("Password", password)
print("Hashed: ", hashed)

password2 = b"sss"

# Verifying the password
if bcrypt.checkpw(password2, hashed):
 print("Password is correct")
else:
 print("Password is incorrect")