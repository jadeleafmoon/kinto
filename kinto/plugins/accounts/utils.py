import bcrypt


ACCOUNT_CACHE_KEY = "accounts:{}:verified"
ACCOUNT_POLICY_NAME = "account"
ACCOUNT_VALIDATION_CACHE_KEY = "accounts:{}:validation-key"


def hash_password(password):
    # Store password safely in database as str
    # (bcrypt.hashpw returns base64 bytes).
    pwd_str = password.encode(encoding="utf-8")
    hashed = bcrypt.hashpw(pwd_str, bcrypt.gensalt())
    return hashed.decode(encoding="utf-8")


def is_validated(user):
    """Is this user record validated?"""
    # An account is "validated" if it has the `validated` field set to True, or
    # no `validated` field at all (for accounts created before the "account
    # validation option" was enabled).
    return "validated" not in user or user["validated"]
