import re

for filename in ['e:/portfoliosite/index.html', 'e:/portfoliosite/git_version.html']:
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        new_content = content.replace('IIIT Madras', 'IIT Madras')
        new_content = new_content.replace('iiit madras', 'iit madras')
        new_content = new_content.replace('IIIT', 'IIT')

        if content != new_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"SUCCESSFULLY FIXED IIIT -> IIT SPELLING IN {filename}!")
        else:
            print(f"No IIIT instances found in {filename}.")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
