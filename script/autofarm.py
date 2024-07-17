import keyboard
import threading
import time
import pyperclip

def write_coords():
    keyboard.press_and_release('f9')
    time.sleep(1)


def get_clipboard_data():
    write_coords()
    data = pyperclip.paste()
    return data


def get_coordinates():
    global coordinates
    raw_coordinates = get_clipboard_data()
    new_coordinates = raw_coordinates.split(' ')
    coordinates = {
        'x': new_coordinates[0],
        'y': new_coordinates[1],
        'z': new_coordinates[2]
    }
    print(coordinates)
    # time.sleep(5)


time.sleep(3)
get_coordinates()