from vault.manager import load_vault, save_vault, add_entry, view_entries, delete_entry
from stego.lsb_engine import encode_lsb, decode_lsb
from stego.detection import detect_lsb_anomaly
from storage.secure_delete import secure_delete
from config import VAULT_FILE, STEGO_IMAGE, CARRIER_IMAGE


def run():
    pwd = input("Master password: ")
    vault = load_vault(pwd)

    while True:
        print("\n1 Add  2 View  3 Delete  4 Save  5 Hide  6 Extract  7 Detect  8 Wipe  9 Exit")
        ch = input("> ")

        # ➕ Add entry
        if ch == "1":
            add_entry(vault)

        # 👀 View entries
        elif ch == "2":
            view_entries(vault)

        # ❌ Delete entry
        elif ch == "3":
            delete_entry(vault)

        # 💾 Save vault
        elif ch == "4":
            save_vault(vault, pwd)
            print("✅ Vault saved.")

        # 🖼️ Hide vault inside image
        elif ch == "5":
            save_vault(vault, pwd)
            with open(VAULT_FILE, "rb") as f:
                data = f.read()
            encode_lsb(CARRIER_IMAGE, data, STEGO_IMAGE)
            print("🕵️ Vault hidden in image.")

        # 📤 Extract vault from image
        elif ch == "6":
            data = decode_lsb(STEGO_IMAGE)
            with open(VAULT_FILE, "wb") as f:
                f.write(data)
            print("📦 Vault extracted from image.")

        # 🔍 Detect hidden data
        elif ch == "7":
            score = detect_lsb_anomaly(STEGO_IMAGE)
            print(f"Anomaly score: {score:.4f}")

            if score > 0.05:
                print("⚠️ Possible hidden data detected.")
            else:
                print("✔ Image appears clean.")

        # 🔥 Secure wipe
        elif ch == "8":
            confirm = input("⚠️ Securely delete vault & stego image? (yes/no): ")
            if confirm.lower() == "yes":
                secure_delete(VAULT_FILE)
                secure_delete(STEGO_IMAGE)
                print("🔥 Secure wipe complete.")
                vault = {}
            else:
                print("Aborted.")

        # 🚪 Exit
        elif ch == "9":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")
