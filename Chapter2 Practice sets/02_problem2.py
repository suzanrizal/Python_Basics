letter = '''Dear <|name|>,
        You are selected
        <|date|>'''

print(letter.replace("<|name|>", "sujan").replace("<|date|>", "20 September 2026"))