environment = "staging"
is_admin = False

if environment == "prod" and is_admin:
    print("Full access granted")
elif environment == "prod" and not is_admin:
    print("Read-only access")
elif environment == "dev":
    print("Development access")
else:
    print("Unknown environment")
    