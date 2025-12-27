import json
from datetime import datetime

# Valid roles and environments

valid_roles = {"root", "admin", "user", "guest"}
valid_envs = {"prod", "dev"}

# -------------------------------
# 1. Access rules (same as Day 7)
# -------------------------------

access_rules = {
    ("root", "dev"): "full access",
    ("root", "prod"): "full access",
    ("admin", "dev"): "full access",
    ("admin", "prod"): "full access",
    ("user", "dev"): "limited access",
    ("user", "prod"): "read-only access",
    ("guest", "prod"): "read-only access",
}

# -------------------------------
# 2. Reusable function
# -------------------------------

def get_access_level(role, environment):
    role = role.lower()
    environment = environment.lower()
    return access_rules.get((role, environment), "no_access")

# -------------------------------
# 3. Batch of requests to evaluate
# -------------------------------

requests = [
    ("root", "prod"),
    ("admin", "dev"),
    ("user", "prod"),
    ("guest", "prod"),
    ("guest", "dev"),
    ("ADMIN", "DEV"),
    ("guest", "stage"),
    ("manager", "dev"),
    ("IT", "IT"),
]

# -------------------------------
# 4. Evaluate + store results
# -------------------------------

results = []

for role, environment in requests:

    # Normalize input FIRST
    role_norm = role.lower()
    env_norm = environment.lower()

    # Validation checks
    if role_norm not in valid_roles:
        access = "invalid_request"
        valid_flag = False
        reason = f"invalid role: {role}"
    elif env_norm not in valid_envs:
        access = "invalid_request"
        valid_flag = False
        reason = f"invalid environment: {environment}"
    else:
        access = get_access_level(role_norm, env_norm)
        valid_flag = access != "no_access"
        reason = "rule matched" if valid_flag else "no matching rule"

    # Build the record
    record = {
        "role": role_norm,
        "environment": env_norm,
        "access_level": access,
        "valid": valid_flag,
        "reason": reason,
        "timestamp": datetime.now().isoformat()
    }

    # Store result
    results.append(record)

# -------------------------------
# 5. Write full JSON output
# -------------------------------

with open("output.json", "w") as f:
    f.write(json.dumps(results, indent=2))

# -------------------------------
# 6. Append human-readable log
# -------------------------------

with open("log.txt", "a", encoding="utf-8") as f:
    for r in results:
        f.write(f"[{r['timestamp']}] {r['role']} -> {r['environment']} -> {r['access_level']}\n")


print("Evaluation complete. JSON + log written.")
