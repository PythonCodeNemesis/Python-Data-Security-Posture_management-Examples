from passlib.hash import bcrypt
# Hash and salt a password
def hash_password(password):
    hashed_password = bcrypt.hash(password)
    return hashed_password
# Verify a password against a hashed/salted password
def verify_password(password, hashed_password):
    return bcrypt.verify(password, hashed_password)
# Usage example
password = input("Enter a password: ")
hashed_password = hash_password(password)
# Simulate password verification
password_to_check = input("Enter the same password again to verify: ")
is_verified = verify_password(password_to_check, hashed_password)
print("Password verification result:", is_verified)
