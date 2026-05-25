import hashlib
import json

def calculate_hash(data):
    encoded_data = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(encoded_data).hexdigest()