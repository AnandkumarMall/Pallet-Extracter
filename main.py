from tkinter import *
from tkinter import filedialog, messagebox, ttk
import colorgram
import pyperclip

BACKGROUND = '#1F2544'
fonts=("Arial", 15, "bold")
window = Tk()
window.title('Pallet')
window.minsize(width=500, height=500)
window.config(padx=0, pady=0, bg=BACKGROUND)


def display_color(colors):
    color_frame = Frame(window)
    color_frame.config(width=450,height=450)

    # Headings
    heading_color = Label(color_frame, text="Color", font=fonts)
    heading_color.grid(row=0, column=0)

    heading_code = Label(color_frame, text="Code", font=fonts)
    heading_code.grid(row=0, column=1, padx=10)

    heading_percentage = Label(color_frame, text="Percentage", font=fonts)
    heading_percentage.grid(row=0, column=2, padx=10)
    color_frame.pack()
    for i, color_code in enumerate(colors,start=1):
        # Button to represent color
        color_button = Button(color_frame, text='', bg=color_code[0], height=2, width=30,padx=2,pady=2,command=pyperclip.copy(color_code[0]))
        color_button.grid(row=i, column=0)

        color_label = Label(color_frame, text=color_code[0],height=2, width=30,font=fonts,padx=2,pady=2)
        color_label.grid(row=i, column=1)

        # Label to display percentage
        percentage_label = Label(color_frame, text=color_code[1],height=2, width=30,font=fonts,padx=2,pady=2)  
        percentage_label.grid(row=i, column=2)


def extract(image):
    colors = colorgram.extract(image, 10)
    colors = [(f'#{c.rgb.r:02x}{c.rgb.g:02x}{c.rgb.b:02x}', c.proportion) for c in colors]
    display_color(colors)


def select_file():
    selected_file = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=(
            ("Image Files", "*.png;*.jpg;*.jpeg;*.gif"),  # Allow multiple image file extensions
            ("PNG Files", "*.png"),
            ("JPEG Files", "*.jpg;*.jpeg"),
            ("GIF Files", "*.gif"),
        )
    )
    if selected_file:
        extract(selected_file)
    else:
        messagebox.showerror(title="Save Image", message="No file selected.")


open_image_button_image = PhotoImage(file='images/open Image.png')

open_image_button = Button(image=open_image_button_image, highlightthickness=0, command=select_file, bg=BACKGROUND)
open_image_button.pack()

window.mainloop()
