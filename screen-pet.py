from tkinter import HIDDEN, NORMAL, Tk, Canvas
import random
from tkinter.constants import TRUE

def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state = new_state)
    c.itemconfigure(pupil_right, state = new_state)
    c.itemconfigure(eye_left, fill = new_color)
    c.itemconfigure(eye_right, fill = new_color)

def blink():
    toggle_eyes()                                                   # Close the eyes
    root.after(250, toggle_eyes)                                    # Wait 250 milliseconds, then open the eyes
    root.after(3000, blink)                                         # Wait 3000 milliseconds, then blink again

def toggle_left_eye():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(eye_left, fill = new_color)

def wink(event):
    toggle_left_eye()
    root.after(250, toggle_left_eye)

def toggle_pupils():
    if not c.eyes_crossed:                                          # Checks if the eye is already crossed
        c.move(pupil_left, 10, -5)                                  # If the pupils aren't crossed, this line moves them in 
        c.move(pupil_right, -10, -5)                                # If the pupils aren't crossed, this line moves them in
        c.eyes_crossed = True                                       # This line sets a flag variable saying the eyes are crossed
    else:                                                           # The eyes are already crossed (else)
        c.move(pupil_left, -10, 5)                                  # This line moves the pupils back to the normal
        c.move(pupil_right, 10, 5)                                  # This line moves the pupils back to the normal
        c.eyes_crossed = False                                      # This line sets flag saying the eyes aren't crossed

def toggle_tongue():
    if not c.tongue_out:                                            # Checks if the tongue is already out
        c.itemconfigure(tongue_tip, state=NORMAL)                   # If the tongue is not out this code makes it visible
        c.itemconfigure(tongue_main, state=NORMAL)                  # If the tongue is not out this code makes it visible
        c.tongue_out = True                                         # This line sets a flag variable saying the tongue is now out
    else:                                                           # The tongue is already out(else)
        c.itemconfigure(tongue_tip, sate=HIDDEN)                    # This line hide the tongue again
        c.itemconfigure(tongue_main, state=HIDDEN)                  # This line hide the tongue again
        c.tongue_out = False                                        # This line sets the flag variable saying the tongue isn't out

def cheeky(event):
    toggle_tongue()                                                 # Sticks the tongue out
    toggle_pupils()                                                 # cross the pupils
    hide_happy(event)                                               # Hide happy face
    root.after(1000, toggle_tongue)                                 # Put the tongue in after 1000 milliseconds
    root.after(1000, toggle_pupils)                                 # Uncross the pupils after 1000 milliseconds
    return

def show_happy(event):
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(cheek_left, state=NORMAL)                   # Show pink cheeks
        c.itemconfigure(cheek_right, state=NORMAL)                  # Show pink cheeks
        c.itemconfigure(mouth_happy, state=NORMAL)                  # Show happy mouth
        c.itemconfigure(mouth_normal, state=HIDDEN)                 # Hide the normal mouth
        c.itemconfigure(mouth_sad, state=HIDDEN)                    # Hide the sad mouth
        c.happy_level = 10
    return

def hide_happy(event):
    c.itemconfigure(cheek_left, state=HIDDEN)                       # Hide pink cheeks
    c.itemconfigure(cheek_right, state=HIDDEN)                      # Hide pink cheeks
    c.itemconfigure(mouth_happy, state=HIDDEN)                      # Hide the happy mouth
    c.itemconfigure(mouth_normal, state=NORMAL)                     # Show the normal mouth
    c.itemconfigure(mouth_sad, state=HIDDEN)                        # Hide the sad mouth
    return

def sad():
    if c.happy_level == 0:                                          # This line checks to see if the value of c.happy_level is 0
        c.itemconfigure(mouth_happy, state=HIDDEN)                  # If c.happy_level = 0, this code hides the happy and normal expressions
        c.itemconfigure(mouth_normal, state=HIDDEN)                 # If c.happy_level = 0, this code hides the happy and normal expressions    
        c.itemconfigure(mouth_sad, state=NORMAL)                    # This line sets Screen pet's expression to sad
    else:                                                           # The value of c.happy_level is greater than 0(else)
        c.happy_level -= 1                                          # Substract one from the value of c.happy_level
    root.after(5000, sad)                                           # Calls sad() again after 5000 milliseconds

def change_color():
    pet_colors = ['SkyBlue1', 'tomato', 'yellow', 'purple', 'green', 'orange']
    c.body_color = random.choice(pet_colors)
    c.itemconfigure(body, outline=c.body_color, fill=c.body_color) 
    c.itemconfigure(ear_left, outline=c.body_color, fill=c.body_color)
    c.itemconfigure(ear_right, outline=c.body_color, fill=c.body_color)
    c.itemconfigure(foot_left, outline=c.body_color, fill=c.body_color)
    c.itemconfigure(foot_right, outline=c.body_color, fill=c.body_color)
    root.after(5000, change_color)

root = Tk()                                                         # This line starts tkinter and opens a window
c = Canvas(root, width=400, height=400)                             # The canvas will be 400 pixels wide and 400 pixels high
c.configure(bg='darkblue', highlightthickness=0)                    # The backgroung color will be darkblue

c.body_color = 'SkyBlue1'

body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)

ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)

foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)

eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill= 'black')

mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)

cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)


c.pack()                                 # This command aranges things within the tkinter window any commands that starts with c. are related to the canvas

c.bind('<Motion>', show_happy)           # This command links the moving mouse-pointer to the happy face
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>', wink)
c.happy_level = 10
c.eyes_crossed = False                   # This are the flag variables for the pupils and the tongue
c.tongue_out = False

root.after(1000, blink)
root.after(5000, sad)
root.after(5000, change_color)
root.mainloop()                          # This line starts the function that looks out for input events such as a mouth click
