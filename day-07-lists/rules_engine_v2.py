# Day 7: Lists, Validation, and Rule Evaluation at Scale

access_rules = {
    ("root", "dev"): "full access",
    ("root", "prod"): "full access",
    ("admin", "dev"): "full access",
    ("admin", "prod"): "full access",
    ("user", "dev"): "limited access",
    ("user", "prod"): "read-only access",
    ("guest", "prod"): "read-only access"
}

def get_access_level(role, environment):
    role = role.lower()
    environment = environment.lower()
    return access_rules.get((role, environment), "no_access")

def main():
    print("Access Checker v3")
    print("----------------")

requests = [
    ("root", "prod"),
    ("root", "dev"),
    ("admin", "dev"),
    ("user", "prod"),
    ("user", "dev"),
    ("guest", "prod"),
    ("guest", "dev"),
    ("ADMIN", "DEV"),
]

summary = {}

for role, environment in requests:
    access = get_access_level(role, environment)
    print(role, environment, "→", access)

    summary[access] = summary.get(access, 0) + 1

print("\nSummary:")
for access_level, count in summary.items():
    print(access_level, ":", count)


# main()
