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


def on_click(x, y, button, pressed):
    print(button)
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


with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    with open(file, "a") as output:
        listener.join()
