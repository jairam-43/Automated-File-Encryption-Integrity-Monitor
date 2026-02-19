import os
from cryptography.fernet import Fernet

TARGET_FILE = r"E:\Projects\Automated-File-Encryption-Integrity-Monitor\sensitive_data.txt"
KEY_FILE = "secret.key"

def unlock_file():
    
    if not os.path.exists(KEY_FILE):
        print("[!] Error: 'secret.key' not found. Cannot decrypt without it.")
        return

    with open(KEY_FILE, "rb") as f:
        key = f.read()
    
    fernet = Fernet(key)

    try:
        with open(TARGET_FILE, "rb") as f:
            encrypted_data = f.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        with open(TARGET_FILE, "wb") as f:
            f.write(decrypted_data)

        print(f"[+] Success! {TARGET_FILE} has been restored to its original state.")

    except Exception as e:
        print(f"[!] Decryption failed: {e}")
        print("\nFile isn't encrypted or the key is wrong")

if __name__ == "__main__":
    unlock_file()