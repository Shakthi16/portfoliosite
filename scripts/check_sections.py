with open('restored_learning_in_motion.html', encoding='utf-8') as f:
    lm = f.read()

with open('restored_skills_section.html', encoding='utf-8') as f:
    sk = f.read()

print("--- LEARNING IN MOTION ---")
print(lm[:300])

print("--- SKILLS ARSENAL ---")
print(sk[:300])
