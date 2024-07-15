import os

def has_terraform_files():
    terraform_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".tf"):
                terraform_files.append(os.path.join(root, file))
    return terraform_files

if __name__ == "__main__":
    terraform_files = has_terraform_files()
    if terraform_files:
        print(f"Terraform files found: {terraform_files}")
        # Define a saída
        print("::set-output name=terraform_files_found::true")
        exit(0)
    else:
        print("No Terraform files found.")
        # Define a saída
        print("::set-output name=terraform_files_found::false")
        exit(1)
