import re

text = "My phone number is 123-456-7890. Call me!"

# Find the phone number
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print(f"Phone number found from the text: {match.group()}")
else:
    print(f"Phone number found from the text: {match}")

# Find all words starting with 'p'
words_starting_with_p = re.findall(r"\bp\w+", text, re.IGNORECASE)
print(f"Words starting with 'p': {words_starting_with_p}")

# Replace spaces with underscores
new_text = re.sub(r"\s", "_", text)
print(f"Text with underscores: {new_text}")