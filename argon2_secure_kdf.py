from argon2.low_level import Type, hash_secret_raw
import hashlib
import hmac

def randomize_salt(user_salt: bytes) -> bytes:
    """
    Randomizes the user-provided salt by padding it to a fixed length and 
    combining it with additional random bytes using a seeded secure 
    pseudo-random function (PRF).
    """
    if not user_salt:
        raise ValueError("User-provided salt must not be empty.")
    
    # Use HMAC with SHA-256 as a seeded secure PRF
    prf = hmac.new(hashlib.sha256(user_salt).digest(), user_salt, hashlib.sha256)
    
    # Return the randomized salt using HMAC digest
    return prf.digest()

def derive_key(password: str, salt: bytes, time_cost: int = 2, 
               memory_cost: int = 102400, parallelism: int = 8, 
               hash_len: int = 32) -> bytes:
    """
    Derives a key using Argon2 algorithm with user-provided and randomized salt.
    """
    # Validate that salt is provided and not empty
    if not salt:
        raise ValueError("Salt must be provided and cannot be empty.")
    
    # Derive the key using Argon2
    derived_key = hash_secret_raw(
        secret=password.encode('utf-8'),
        salt=salt,
        time_cost=time_cost,      # Number of iterations
        memory_cost=memory_cost,  # Memory usage in kibibytes
        parallelism=parallelism,  # Number of parallel threads
        hash_len=hash_len,        # Length of the derived key
        type=Type.ID             # Use Argon2id variant
    )
    
    return derived_key

# Example usage:
password = "your_password_here"
user_salt = b"User-ID-2"

# Randomize the user-provided salt
randomized_salt = randomize_salt(user_salt)

# Derive the key with enhanced security parameters
derived_key = derive_key(password, randomized_salt, 
                        time_cost=5, memory_cost=65536, 
                        parallelism=4, hash_len=32)

print(f"Derived Key (hex): {derived_key.hex()}")
print(f"User Salt (hex): {user_salt.hex()}")
print(f"Randomized Salt (hex): {randomized_salt.hex()}")