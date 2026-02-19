# Automated File Encryption & Integrity Monitor

A proactive security tool designed to monitor a specific sensitive file for unauthorized changes. It uses **SHA-256** hashing to detect modifications and automatically secures the file using **AES-256 (Fernet)** encryption if tampering is detected.

## 🚀 Features
* **Real-time Monitoring:** Continuously checks file integrity every 5 seconds.
* **Cryptographic Baselines:** Uses SHA-256 to create a unique digital fingerprint of the target file.
* **Automated Incident Response:** Instantly encrypts the file upon detection of unauthorized changes to prevent data exfiltration or further tampering.
* **Recovery Logic:** Includes a dedicated decryption script to restore the file once the threat is mitigated.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/jairam-43/Automated-File-Encryption-Integrity-Monitor.git](https://github.com/jairam-43/Automated-File-Encryption-Integrity-Monitor.git)
   cd Automated-File-Encryption-Integrity-Monitor

   Set up a Virtual Environment:

Bash
python -m venv .venv
# Activate on Windows:
.venv\Scripts\activate
Install Dependencies:

Bash
pip install -r requirements.txt
📋 Usage
1. Configure the Target
Update the TARGET_FILE path in main.py and unlock.py to point to the file you wish to monitor.

2. Start the Monitor
Run the main script to begin surveillance:

Bash
python main.py
The script creates a baseline hash. If the file is modified, the monitor will detect the mismatch and trigger the encryption lock.

3. Restore the File
To decrypt the file and return it to its original state:

Bash
python unlock.py



License
This project is for educational purposes.


---

### Final Push Instructions
Now that you have your `README.md` and `requirements.txt`, run these three commands to finish your GitHub setup:

1. `git add README.md requirements.txt`
2. `git commit -m "Add documentation and dependencies"`
3. `git push origin main`
