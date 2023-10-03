import subprocess

# Function to install dependencies from requirements.txt
def install_requirements():
    try:
        subprocess.check_call(['pip3', 'install', '-r', 'requirements.txt'])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install dependencies. Check if 'pip' is installed and 'requirements.txt' exists.")

# Function to run main.py
def run_main():
    try:
        subprocess.check_call(['python3', 'src/main.py'])
    except subprocess.CalledProcessError:
        print("Failed to run 'main.py'.")

if __name__ == "__main__":
    install_requirements()  # Install dependencies from requirements.txt
    run_main()              # Run main.py
