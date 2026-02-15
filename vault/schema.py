def validate_entry(entry):
    required = {"site", "username", "password"}
    return required.issubset(entry.keys())
