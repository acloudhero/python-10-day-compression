# Day 6: Data-driven access rules

access_rules = {
    ("root", "dev"): "full access",
    ("root", "prod"): "full access",
    ("admin", "dev"): "full access",
    ("admin", "prod",): "full access",
    ("user", "dev"): "limited access",
    ("user", "prod"): "read-only access",
    ("guest", "prod"): "read-only access"
}

def get_access_level(role, environment):
    return access_rules.get((role, environment), "no access")

def main():
    print("Access Checker v2")
    print("----------------")

    runs = 0

    while True:
        role = input("Enter role (admin/user/guest or quit): ")
        role = role.lower()
        if role == "quit":
            print("Total checks performed:", runs)
            print("Exiting.")
            break

        environment = input("Enter environment (prod/dev): ")
        environment = environment.lower()


        access = get_access_level(role, environment)
        print("Access level:", access)

        runs += 1
        print("Checks performed:", runs)
        print()

main()
