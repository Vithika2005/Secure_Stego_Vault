from vault.manager import load_vault, save_vault, add_entry, list_entries

def test_vault():
    password = "master123"

    vault = load_vault(password)

    add_entry(vault, "gmail", "user@gmail.com", "pass123")
    add_entry(vault, "github", "dev", "ghp_xxx")

    save_vault(vault, password)

    vault2 = load_vault(password)
    print("Vault contents:", list_entries(vault2))

if __name__ == "__main__":
    test_vault()
