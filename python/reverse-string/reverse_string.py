def reverse(text = ""):
    if text == "":
        return ""

    reverseText = ""

    for char in text:
        reverseText = char + reverseText

    return reverseText
