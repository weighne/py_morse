import pynput
from pynput import mouse
from pynput.mouse import Listener
from morse_config import alphabet
import sys

# --- Definitions ---

phrase = []
file = "msg.txt"
translate_file = "msg_translated.txt"

# --- Ignore these functions, they exist to make the mouse listener happy ---

def on_move(x, y):
    pass


def on_scroll(x, y, dx, dy):
    pass

# --- Actually important functions ---

def translate(phrase):
    letter = "".join(phrase).strip()

    with open(translate_file, "a") as translate_out:
        for x in alphabet:
            if letter == x:
                translate_out.write(alphabet[x])
            else:
                continue

    phrase.clear()


def text_to_morse(phrase):
    translated_phrase = []
    for letter in phrase:
        for x in alphabet:
            if letter.upper() == alphabet[x]:
                translated_phrase.append(x)
            elif letter == " ":
                translated_phrase.append("/")
            else:
                continue

    return " ".join(translated_phrase)


def morse_to_text(morse):
    morse_phrase = morse.split(" ").strip()
    translated_phrase = []
    for x in morse_phrase:
        for y in alphabet:
            if x == y:
                translated_phrase.append(alphabet[x])
            elif x == " ":
                translated_phrase.append(" ")
            else:
                continue

    return "".join(translated_phrase)


def on_click(x, y, button, pressed):
    sys.stdout.write("")
    try:
        if button == mouse.Button.left and pressed == True:
            output.write("-")
            phrase.append("-")
        elif button == mouse.Button.right and pressed == True:
            output.write(".")
            phrase.append(".")
        elif button == mouse.Button.middle and pressed == True:
            output.write(" ")
            phrase.append(" ")
        elif button == mouse.Button.middle and pressed == False:
            output.write("")
            translate(phrase)
            #translate the letter
        else:
            sys.stdout.write("")
    except IndexError:
        sys.stdout.write("")

choice = 0
print("Welcome to Py_Morse!")
print("TIP: Use \'Ctrl+C\' to kill this script at any point!")
while choice == 0:
    try:
        print("\nWhat would you like to do?\n1 - Translate text to morse\n2 - Translate morse to text\n3 - Write morse")
        choice = int(input("Input:"))
    except ValueError:
        choice = 0

if choice == 1:
    print("Input your string:")
    user_string = input()
    print(text_to_morse(user_string))
elif choice == 2:
    print("Input your morse:")
    user_string = input()
    print(morse_to_text(user_string))
elif choice == 3:
    print("Morse output will be written to \'msg.txt\'\nPlaintext output will be written to \'msg_translated.txt\'\nLeft-Click = -\nRight-Click = .\nMiddle-Click = Space\n")
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        with open(file, "a") as output:
            listener.join()
