import subprocess

print("Running insert_all_sections_after_home.py...")
exec(open('insert_all_sections_after_home.py', encoding='utf-8').read())

print("Running restore_journey_section.py...")
exec(open('restore_journey_section.py', encoding='utf-8').read())

print("Done restoring full portfolio sections!")
