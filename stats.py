def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_list = []
    for letter in text:
        if letter.isalpha():
            found = False
            for item in letter_list:
                if item["char"] == letter.lower():
                    item["num"] += 1
                    found = True
                    break
            if not found:
                letter_list.append({"char": letter.lower(), "num": 1})
    letter_list.sort(key=lambda x: x["num"], reverse=True)
    return letter_list
