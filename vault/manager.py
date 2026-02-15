import json
from crypto.aes_gcm import encrypt, decrypt
from storage.file_store import read_file, write_file
from config import VAULT_FILE
from vault.audit_log import log_event


def load_vault(password):
    try:
        blob = read_file(VAULT_FILE)
        data = decrypt(blob, password)
        vault = json.loads(data)
        log_event("LOAD_VAULT")
        return vault
    except FileNotFoundError:
        log_event("INIT_VAULT")
        return []
    except Exception:
        log_event("FAILED_LOGIN")
        raise ValueError("Invalid password or corrupted vault")


def save_vault(vault, password):
    data = json.dumps(vault).encode()
    blob = encrypt(data, password)
    write_file(VAULT_FILE, blob)
    log_event("SAVE_VAULT")


def add_entry(vault):
    site = input("Site: ")
    user = input("Username: ")
    pwd = input("Password: ")

    vault.append({"site": site, "username": user, "password": pwd})
    log_event("ADD_ENTRY", site)


def view_entries(vault):
    for i, e in enumerate(vault, 1):
        print(f"{i}. {e['site']} | {e['username']} | {e['password']}")


def delete_entry(vault):
    view_entries(vault)
    idx = int(input("Delete #: ")) - 1

    if 0 <= idx < len(vault):
        site = vault[idx]["site"]
        vault.pop(idx)
        log_event("DELETE_ENTRY", site)
