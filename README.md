# Secure Argon2 Implementation

A production-ready Python implementation of Argon2 key derivation with enhanced security features including salt randomization and optimal parameter configuration.

## Overview

This repository demonstrates secure password-based key derivation using Argon2, the winner of the Password Hashing Competition (2013-2015). The implementation goes beyond basic Argon2 usage by incorporating advanced security practices that are applicable across all programming languages.

## Features

- 🛡️ **Salt Randomization**: HMAC-SHA256 based salt processing for enhanced security
- 🎯 **Argon2id Implementation**: Hybrid variant providing balanced protection against GPU and side-channel attacks
- ⚡ **Configurable Parameters**: Tunable time cost, memory cost, and parallelism settings
- 🔍 **Input Validation**: Comprehensive error handling and input sanitization
- 📝 **Production Ready**: Conservative defaults with guidance for security optimization

## Quick Start

### Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Basic Usage

```python
from argon2_secure import randomize_salt, derive_key

# Your password and user identifier
password = "your_secure_password"
user_salt = b"User-ID-123"

# Randomize the salt for enhanced security
randomized_salt = randomize_salt(user_salt)

# Derive key with secure parameters
derived_key = derive_key(
    password=password,
    salt=randomized_salt,
    time_cost=5,        # Adjust based on performance requirements
    memory_cost=65536,  # 64 MB - increase for higher security
    parallelism=4,      # Adjust based on available CPU cores
    hash_len=32        # 256-bit key length
)

print(f"Derived Key: {derived_key.hex()}")
```

## Security Features Explained

### Salt Randomization

The `randomize_salt()` function processes user-provided salts through HMAC-SHA256 to ensure:

- **Uniform entropy distribution** regardless of input salt quality
- **Fixed-length output** (32 bytes) for consistent security properties
- **Deterministic but unpredictable** results that prevent rainbow table attacks

### Argon2id Variant

This implementation uses Argon2id (hybrid variant) which provides:

- **GPU resistance** through data-dependent memory access patterns
- **Side-channel protection** via data-independent access in initial iterations
- **Balanced security** suitable for most production environments

### Parameter Guidelines

| Parameter     | Default | Production Min | High Security | Description          |
| ------------- | ------- | -------------- | ------------- | -------------------- |
| `time_cost`   | 2       | 3              | 5+            | Number of iterations |
| `memory_cost` | 102400  | 65536          | 131072+       | Memory usage (KiB)   |
| `parallelism` | 8       | 1              | 4-8           | Thread count         |
| `hash_len`    | 32      | 32             | 32-64         | Output key length    |

## File Structure

```
├── argon2_secure_kdf.py      # Main implementation
├── README.md
└── requirements.txt          # Dependencies
```

## API Reference

### `randomize_salt(user_salt: bytes) -> bytes`

Randomizes a user-provided salt using HMAC-SHA256.

**Parameters:**

- `user_salt` (bytes): User-provided salt (must not be empty)

**Returns:**

- bytes: 32-byte randomized salt

**Raises:**

- `ValueError`: If user_salt is empty

### `derive_key(password, salt, time_cost=2, memory_cost=102400, parallelism=8, hash_len=32) -> bytes`

Derives a cryptographic key using Argon2id algorithm.

**Parameters:**

- `password` (str): Password to derive key from
- `salt` (bytes): Salt for key derivation (use randomized salt)
- `time_cost` (int): Number of iterations (default: 2)
- `memory_cost` (int): Memory usage in KiB (default: 102400)
- `parallelism` (int): Number of parallel threads (default: 8)
- `hash_len` (int): Desired key length in bytes (default: 32)

**Returns:**

- bytes: Derived cryptographic key

**Raises:**

- `ValueError`: If salt is empty or invalid parameters provided

## Security Considerations

### Parameter Tuning

1. **Benchmark on target hardware** to find optimal performance/security balance
2. **Start conservative** and increase parameters gradually
3. **Monitor authentication timing** in production
4. **Plan for parameter upgrades** as hardware evolves

### Threat Model

This implementation protects against:

- ✅ Rainbow table attacks
- ✅ Dictionary attacks
- ✅ GPU-based brute force
- ✅ ASIC-based attacks
- ✅ Side-channel attacks
- ✅ Time-memory trade-off attacks

### Production Deployment

- Use **minimum 64MB memory cost** for production systems
- Implement **rate limiting** on authentication endpoints
- Consider **adaptive parameters** based on user risk profiles
- Regularly **review and update** security parameters

## Language Portability

While this implementation uses Python, the security principles and architecture translate directly to other languages:

- **Java**: Use Spring Security Crypto or Bouncy Castle
- **C#**: Use .NET's System.Security.Cryptography with Argon2
- **Go**: Use golang.org/x/crypto/argon2
- **Node.js**: Use the 'argon2' npm package
- **Rust**: Use the 'argon2' crate

## Performance Benchmarks

Approximate timing on modern hardware (adjust parameters accordingly):

| Memory (MB) | Time Cost | Threads | Duration | Security Level |
| ----------- | --------- | ------- | -------- | -------------- |
| 64          | 3         | 4       | ~500ms   | Standard       |
| 128         | 4         | 4       | ~1000ms  | High           |
| 256         | 5         | 8       | ~1500ms  | Maximum        |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/security-enhancement`)
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## Related Resources

- 📖 **Detailed Article**: [Secure Key Derivation with Argon2 on Medium]([MEDIUM_LINK_PLACEHOLDER])
- 🔗 **Argon2 Specification**: [RFC 9106](https://tools.ietf.org/rfc/rfc9106.txt)
- 🏆 **Password Hashing Competition**: [Official PHC Site](https://password-hashing.net/)
- 📚 **OWASP Password Storage**: [Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Security Notice

This implementation is provided for educational and production use. While following security best practices, always conduct thorough security reviews and testing before deploying in critical systems.

---

**Author**: Mohamed Ahmed Gebril
**Blog**: https://medium.com/@moh.ahmed.gebril/secure-key-derivation-with-argon2-a-modern-approach-to-password-based-cryptography-ba18e762fc25
