# THis progrom moves the mouse not drags over by some distance upon clicking.

from pynput.mouse import Controller, Listener

# Initialize the mouse controller
mouse = Controller()

# Global variable to track the mouse button pressed state
is_mouse_pressed = False

# Callback function for mouse press event 
def on_mouse_press(x, y, button, pressed):
    global is_mouse_pressed
    if button == button.left:
        is_mouse_pressed = pressed
        if is_mouse_pressed:
            # Get the current mouse position
            current_x, current_y = mouse.position
            # Calculate the new position 50 pixels to the right
            new_x = current_x + 50
            # Move the mouse to the new position
            mouse.position = (new_x, current_y)

# Callback function for mouse move event
def on_mouse_move(x, y):
    pass  # Do nothing for mouse move events

# Start the mouse listener
with Listener(on_click=on_mouse_press, on_move=on_mouse_move) as listener:
    listener.join()
