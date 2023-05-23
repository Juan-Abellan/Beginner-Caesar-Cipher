from art import logo

still = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(_direction, _text, _shift):
    output_text = ""

    if _direction == "decode":
        _shift = _shift * -1

    for letter in _text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if index + _shift > 25:
                output_text += alphabet[(index + _shift) - 25 - 1]
            elif letter in alphabet:
                output_text += alphabet[index + _shift]
        elif letter == " ":
            output_text += " "
        else:
            output_text += letter

    return f"{_text} |  {_direction} text is ---> {output_text} <---\n"


print(logo)
while still:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    print(caesar(_direction=direction, _text=text, _shift=shift))
    answer = input("still playing around? yes or no\n")
    if answer == "no":
        still = False
        print("ciao!")
