import os

def has_terraform_files():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".tf"):
                return True
    return False

if __name__ == "__main__":
    if has_terraform_files():
        print("Terraform files found.")
        exit(0)
    else:
        print("No Terraform files found.")
        exit(1)
