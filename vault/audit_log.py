import json
from datetime import datetime
from pathlib import Path

AUDIT_LOG_FILE = Path("data/audit.log")

def log_event(action: str, details: str = ""):
    AUDIT_LOG_FILE.parent.mkdir(exist_ok=True)

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action,
        "details": details,
    }

    with open(AUDIT_LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
