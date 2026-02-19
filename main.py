import hashlib, os, time
from cryptography.fernet import Fernet


TARGET_FILE = r"E:\Projects\Automated-File-Encryption-Integrity-Monitor\sensitive_data.txt"
KEY_FILE = "secret.key"

def get_hash(filename):
    
    with open(filename, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def lock_file(filename):
    
    if not os.path.exists(KEY_FILE):
        with open(KEY_FILE, "wb") as f: 
            f.write(Fernet.generate_key())
    
    key = open(KEY_FILE, "rb").read()
    fernet = Fernet(key)

    with open(filename, "rb") as f: 
        original_data = f.read()

    encrypted_data = fernet.encrypt(original_data)
    
    with open(filename, "wb") as f: 
        f.write(encrypted_data)

def monitor():
    if not os.path.exists(TARGET_FILE):
        print(f"[!] Error: System cannot find the file at {TARGET_FILE}")
        return

    baseline_hash = get_hash(TARGET_FILE)
    print(f"[*] SOC Monitor Active on: {TARGET_FILE}")
    print(f"[*] Baseline SHA-256: {baseline_hash}\n")

    try:
        while True:
            time.sleep(5)
            current_hash = get_hash(TARGET_FILE)

            if current_hash != baseline_hash:
                print("\n[!!!] ALERT: UNAUTHORIZED CHANGE DETECTED!")
                lock_file(TARGET_FILE)
                print(f"[+] Security Action: {TARGET_FILE} has been encrypted.")
                break 
            else:
                print("Checking... [SAFE]", end="\r")
                
    except KeyboardInterrupt:
        print("\n[*] Monitoring stopped by user.")

if __name__ == "__main__":
    monitor()