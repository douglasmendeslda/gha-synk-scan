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
        # Define a saída usando arquivos de ambiente
        with open(os.environ['GITHUB_ENV'], 'a') as env_file:
            env_file.write("TERRAFORM_FILES_FOUND=true\n")
        exit(0)
    else:
        print("No Terraform files found.")
        # Define a saída usando arquivos de ambiente
        with open(os.environ['GITHUB_ENV'], 'a') as env_file:
            env_file.write("TERRAFORM_FILES_FOUND=false\n")
        exit(1)
