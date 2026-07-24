import json
with open(r'C:\Users\sssum\.gemini\antigravity-ide\brain\7394872a-c4c7-4df7-8be9-a014f3404d19\.system_generated\logs\transcript.jsonl', encoding='utf-8') as f:
    lines = f.readlines()
print('Total lines:', len(lines))

# search for steps containing 'torn' or 'timeline-container' or 'node-hero' in content
for i, raw in enumerate(lines):
    try:
        obj = json.loads(raw)
        content = str(obj)
        if 'torn-paper' in content or 'node-hero' in content or 'timeline-container' in content:
            print(f'Step {i}: type={obj.get("type")} source={obj.get("source")}')
    except:
        pass
