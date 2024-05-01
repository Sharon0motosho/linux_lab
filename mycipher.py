import sys

encrypted_text = ""
letter_count = 0
line_count = 0

shift = int(sys.argv[1])

input_text = sys.stdin.read()


for char in input_text:
    if char.isalpha():
        char = char.upper()
        encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        letter_count += 1
        line_count += 1

    if letter_count == 5:
        encrypted_text += " "
        letter_count = 0

    if line_count == 50:
        encrypted_text += "\n"
        line_count = 0

print (encrypted_text)


