import json
import re

def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression to match the details and summary content
    pattern = re.compile(r'<details><summary>(.*?)</summary>(.*?)</details>', re.DOTALL)
    matches = pattern.findall(content)

    tips = []
    for match in matches:
        # remove leading number with . and space from summary we should have used a better regex

        summary = match[0].strip().split('. ', 1)[1]
        content = match[1].strip()
        tips.append({"summary": summary, "content": content})

    return tips

def save_to_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    markdown_file = 'README.md'
    json_file = 'tips.json'

    tips = parse_markdown(markdown_file)
    save_to_json(tips, json_file)
    print(f"Converted {len(tips)} tips to JSON and saved to {json_file}")
