import os
import sys

def check_terraform_files():
    # Lógica para verificar arquivos Terraform
    terraform_files_found = True  # Simulação de verificação
    return terraform_files_found

def main():
    if len(sys.argv) != 3:
        print("Uso: python check_terraform_files.py <snyk_token> <github_token>")
        sys.exit(1)
    
    snyk_token = sys.argv[1]
    github_token = sys.argv[2]

    terraform_files_found = check_terraform_files()

    if terraform_files_found:
        os.system(f"snyk auth {snyk_token}")
        os.system("snyk iac test > snyk_output.txt || true")
        
        with open("snyk_output.txt", "r") as file:
            output = file.read()

        if output.strip():
            print("Snyk test output:")
            print(output)
            # Aqui você pode adicionar a lógica para decorar a pull request

        else:
            print("Snyk test output is empty. Exiting.")
            sys.exit(1)
    else:
        print("No Terraform files found. Exiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()
