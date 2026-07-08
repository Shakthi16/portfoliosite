import subprocess

try:
    subprocess.run(["C:\\Program Files\\Git\\cmd\\git.exe", "add", "-A"], check=True)
    subprocess.run(["C:\\Program Files\\Git\\cmd\\git.exe", "commit", "-m", "Applying massive Pinterest visual updates and ensuring all files sync"], check=True)
    subprocess.run(["C:\\Program Files\\Git\\cmd\\git.exe", "push", "origin", "main"], check=True)
    print("Git operations successful!")
except Exception as e:
    print(f"Error: {e}")
