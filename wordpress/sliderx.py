import re

# Read the HTML content
with open("rv_service.html", "r", encoding="utf-8") as f:
    html = f.read()

# Define regex to capture all <img ... src="..."> tags
img_tags = re.findall(r'<img[^>]+src="[^"]+"', html)

# Define the 4-image start sequence (as substrings)
start_sequence = [
    'src="https://cabear.com/wp-content/uploads/2024/07/cabear-e1720298696709.png"',
    'src="https://cabear.com/wp-content/uploads/2024/07/cabear-e1720298696709.png"',
    'src="https://cabear.com/wp-content/uploads/2024/08/bearpawCircle-1.png"',
    'src="https://cabear.com/wp-content/uploads/2024/08/bearCircle.png"',
]

# Group image tags into sets based on start sequence
sets = []
i = 0
while i < len(img_tags) - 3:
    if all(start_sequence[j] in img_tags[i + j] for j in range(4)):
        img_set = []
        while i < len(img_tags):
            img_set.append(img_tags[i])
            i += 1
            # Stop the set if the next 4 match the start again (next group)
            if all(i + j < len(img_tags) and start_sequence[j] in img_tags[i + j] for j in range(4)):
                break
        sets.append(img_set)
    else:
        i += 1

# Output
for idx, s in enumerate(sets):
    print(f"\n--- Set {idx + 1} ({len(s)} images) ---")
    for img in s:
        src_match = re.search(r'src="([^"]+)"', img)
        if src_match:
            print(src_match.group(1))
