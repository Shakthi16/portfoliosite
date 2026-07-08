import subprocess

try:
    # Revert the last commit
    subprocess.run(["C:\\Program Files\\Git\\cmd\\git.exe", "revert", "HEAD", "--no-edit"], check=True)
    # Push the revert commit
    subprocess.run(["C:\\Program Files\\Git\\cmd\\git.exe", "push", "origin", "main"], check=True)
    print("Successfully reverted the last commit and pushed to origin.")
except subprocess.CalledProcessError as e:
    print(f"Error executing git command: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
