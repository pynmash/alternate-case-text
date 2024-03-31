
def alternate_text(text):
    """
    Alternate the case of the leters in a string
    e.g 'ThIs iS A sTrInG
    """
    text = text.lower()
    new_text = ""

    for i in range(0, len(text)):
        if i % 2 == 0:
            new_text += text[i]
        else:
            new_text += text[i].upper()
    return new_text


if __name__ == "__main__":
    text = "This is sample text"
    print(alternate_text(text))
