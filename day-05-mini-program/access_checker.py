# Day 5: Rules-driven access checker
def get_access_level(role, environment):
    if role == "admin" and environment == "dev":
        return "full access"
    elif role == "admin" and environment == "prod":
        return "full access"
    elif role == "user" and environment == "dev":
        return "limited access"
    elif role == "user" and environment == "prod":
        return "read-only access"
    elif role == "guest" and environment == "prod":
        return "read-only access"
    else:
        return "no access"
# realized this branch explosion is unsustainable there is a more elegant and efficent way to code this

def main():
    print("Access Checker v1")
    print("--------------")

    runs = 0

    while True:
        role = input("Enter role (admin/user/guest or quit): ")
        if role == "quit":
            print("Total checks performed:", runs)
            # if i put "Exiting." before the "total checks...", total checks wont print
            print("Exiting.")
            break

        environment = input("Enter environment (prod/dev): ")

        access = get_access_level(role, environment)
        print("Access level:", access)
        runs += 1
        print("Checks performed:", runs)
        print()
main()
