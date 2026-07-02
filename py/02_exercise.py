text = """Python is a powerful programming language, It's easy to learn
and versatile! You can use Python for web development, data science
, and automation. The syntax is clean and readable. This makes
Python perfect for beginners and experts alike."""

char_count = len(text)
char_count_no_spaces = len(text.replace(" ", ""))
word_count = len(text.split())
sentence_count = text.count(".") + text.count("!") + text.count("?")

print(f"Character count (including spaces): {char_count}")
print(f"Character count (excluding spaces): {char_count_no_spaces}")
print(f"Word count: {word_count}")
print(f"Sentence count: {sentence_count}")