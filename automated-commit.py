import os
import time
import subprocess
from datetime import datetime

# Define the repository directory and GitHub credentials
repo_dir = r'E:\Project\Python\github-automation'  # Replace with your repo path
github_username = 'manuj-rai'  # Replace with your GitHub username
github_token = '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'  # Replace with your GitHub personal access token
repo_name = 'automation'
commit_message = "Automated commit to increase contribution graph"  # Commit message

# Change to the repository directory
os.chdir(repo_dir)

# Function to make changes to a file (example: modify README)
def make_changes():
    # Open the README file or any other file you want to modify
    with open("index.html", "a") as f:
        f.write(f"\nAutomated update on {datetime.now()}\n")

# Function to run Git commands
def git_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error: {result.stderr.decode()}")
    else:
        print(f"Success: {result.stdout.decode()}")

# Function to commit and push changes to GitHub
def commit_and_push():
    # Stage the changes
    git_command("git add .")

    # Commit the changes
    git_command(f'git commit -m "{commit_message}"')

    # Push the changes
git_command(f"git push https://manuj-rai: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@github.com/manuj-rai/automation.git")

# Main function to run the automation
def run_automation():
    while True:
        make_changes()  # Modify the file
        commit_and_push()  # Commit and push the changes
        print(f"Committed at {datetime.now()}")

# Run the automation
run_automation()
