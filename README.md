# 🔐 Secure Stego Vault
**A Steganographic Password Manager with Strong Encryption, Tamper Detection, and Forensic-Resistant Storage**

Secure Stego Vault is a CLI-based security tool that encrypts credentials and hides them inside images using steganography. It also supports steganalysis, secure deletion, audit logging, and a simulated post-quantum hybrid encryption pipeline.

---

## 📌 Features

### 🔐 Cryptography
- AES-256-GCM authenticated encryption
- Argon2 password-based key derivation
- Integrity verification (MAC)
- Simulated Post-Quantum hybrid encryption

### 🗄️ Vault Management
- Add, view, delete credentials
- Encrypted vault storage (`vault.enc`)
- Master password protection

### 🖼️ Steganography
- Hide encrypted vault inside PNG images
- Extract vault from carrier image
- Covert storage and recovery

### 🕵️ Steganalysis
- Detect hidden data in images
- LSB anomaly scoring
- Useful for digital forensics & red-team analysis

### 🧾 Audit Logging
- Tamper-evident logs of vault activity
- Tracks add, delete, load, save operations

### 🧹 Secure Deletion
- Overwrites files before removal
- Prevents forensic recovery

---

## 🏗️ Project Structure

secure-stego-vault/
│
├── main.py
├── config.py
│
├── crypto/
│ ├── aes_gcm.py
│ ├── kdf_argon2.py
│ ├── integrity.py
│ └── pqc_wrapper.py
│
├── vault/
│ ├── manager.py
│ ├── schema.py
│ └── audit_log.py
│
├── stego/
│ ├── lsb_engine.py
│ ├── carrier_utils.py
│ └── detection.py
│
├── storage/
│ ├── file_store.py
│ └── secure_delete.py
│
├── cli/
│ └── menu.py
│
├── tests/
│ ├── test_crypto.py
│ ├── test_vault.py
│ ├── test_stego.py
│ └── test_pqc.py
│
├── assets/sample.png
└── data/
├── vault.enc
└── vault.png


---

## ⚙️ How It Works

### Encryption Flow
Master Password
↓
Argon2 KDF
↓
AES-GCM Encryption
↓
vault.enc


### Steganography Flow
vault.enc
↓
LSB Encoding
↓
vault.png (carrier image)


### Recovery Flow
vault.png
↓
LSB Decoding
↓
vault.enc
↓
AES-GCM Decryption
↓
Credentials Restored


---

## 🧪 CLI Menu

1 Add 2 View 3 Delete 4 Save
5 Hide 6 Extract 7 Detect 8 Wipe 9 Exit

### Hide vault inside image
5
Vault hidden in image.


### Extract vault from image
6
Vault extracted.


### Detect hidden data
7
Anomaly score: 0.0812
⚠ Possible hidden data detected.


---

installation:
  steps:
    - title: Clone Repository
      commands:
        - git clone https://github.com/Vithika2005/Secure_Stego_Vault.git
        - cd secure-stego-vault

    - title: Create Virtual Environment
      commands:
        - python3 -m venv venv
        - source venv/bin/activate

    - title: Install Dependencies
      commands:
        - pip install cryptography argon2-cffi pillow pycryptodome

running:
  command: python main.py

security_value:
  - Secure credential storage using encryption and key derivation
  - Covert data hiding via LSB steganography
  - Digital forensics techniques (steganalysis and anomaly detection)
  - Tamper detection using hashing and integrity checks
  - Post-quantum awareness via hybrid PQC wrapper (simulated)
  - Forensic-resistant deletion using multi-pass secure wipe

limitations:
  - PQC module is simulated and not production-grade
  - LSB steganography can be detected by advanced steganalysis
  - CLI-only interface (no GUI yet)

future_improvements:
  - Real PQC integration (Kyber / Dilithium)
  - Risk engine for threat scoring
  - Multi-image secret sharing
  - GUI interface
  - Hardware key support (YubiKey / TPM)

why_this_project_matters: >
  Modern attackers do not just steal data — they scan for it. This vault explores
  how secrets can be hidden, detected, protected, and destroyed beyond recovery.
  It blends cryptography, steganography, and digital forensics into one practical
  security tool.