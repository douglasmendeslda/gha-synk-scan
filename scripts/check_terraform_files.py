import os
import subprocess

def main():
    try:

        subprocess.run(['git', 'fetch', 'origin', 'main'], check=True)

        subprocess.run(['git', 'merge', 'origin/main', '--no-commit', '--no-ff'], check=True)

        result = subprocess.run(['git', 'diff', '--name-only', 'HEAD'], check=True, capture_output=True, text=True)
        changed_files = result.stdout.splitlines()


        has_terraform = any(file.endswith('.tf') for file in changed_files)

        if has_terraform:
            print("Terraform files detected.")
            exit(0)
        else:
            print("No Terraform files detected.")
            exit(1)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while checking for Terraform files: {e}")
        exit(1)

if __name__ == "__main__":
    main()
