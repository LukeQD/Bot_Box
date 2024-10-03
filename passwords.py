import os
import hashlib
 
def create_secure_password(password):
  salt = os.urandom(16)
  iterations = 100_000 
  hash_value = hashlib.pbkdf2_hmac(
    'sha256',  
    password.encode('utf-8'), 
    salt, 
    iterations
  )
  password_hash = salt + hash_value
  return password_hash
 
print(create_secure_password("HelloWorld"))