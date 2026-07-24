with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', text)
print("Sections found in index.html in order:")
for idx, s in enumerate(sections):
    print(f" {idx+1}. {s}")

print("\nVerifying Work Experiences content in timeline-pin-section:")
assert "IIT Madras" in text
assert "CYSTAR Lab" in text
assert "OpsIntellix" in text
assert "Focuslogic IT Services" in text
assert "Cybersecurity Research Intern" in text
assert "Operations Intern — AP Automation" in text
assert "Web Development Intern" in text
assert "Jul 2025 – May 2026" in text
assert "Nov 2025 – Feb 2026" in text
assert "Mar 2025 – May 2025" in text
assert "Key Duties" in text
assert "openDutyModal" in text
print("ALL VERIFICATIONS PASSED SUCCESSFULLY!")
