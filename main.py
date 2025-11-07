import tkinter as tk
from PIL import Image, ImageTk

# ---------------------- CONSTANTS ----------------------
BGCOLOR = "#FFF176"
BTNCOLOR = "#FFD54F"
FONT1 = ("Arial", 18)
FONT2 = ("Pokemon Hollow", 40, "bold")
FONTBTN = ("Pokemon Hollow", 18, "bold")


# ---------------------- FUNCTIONS ----------------------
def clicked(frame):
    """Raise the selected frame to the top."""
    frame.tkraise()


def on_click(value):
    """Handle calculator button clicks."""
    current = calc_display.get()

    if value == "=":
        try:
            result = eval(current)
            calc_display.delete(0, tk.END)
            calc_display.insert(0, str(result))
        except ZeroDivisionError:
            calc_display.delete(0, tk.END)
            calc_display.insert(0, "Error: Div by 0")
        except Exception:
            calc_display.delete(0, tk.END)
            calc_display.insert(0, "Error")
    elif value == "C":
        calc_display.delete(0, tk.END)
    else:
        calc_display.insert(tk.END, value)


# ---------------------- WINDOW SETUP ----------------------
window = tk.Tk()
window.title("PIKALKULATOR")
window.configure(background=BGCOLOR)
window.geometry("600x500")


# ---------------------- FRAMES ----------------------
frame1 = tk.Frame(window, bg=BGCOLOR)
frame1.place(relwidth=1, relheight=1)

frame2 = tk.Frame(window, bg=BGCOLOR)
frame2.place(relwidth=1, relheight=1)


# ---------------------- CALCULATOR (Frame 2) ----------------------
# Display bar
calc_display = tk.Entry(
    frame2,
    font=("Arial", 24),
    justify="right",
    relief="solid",
    bd=2
)
calc_display.place(relx=0.5, y=60, width=400, height=50, anchor="center")

# ✅ Create a centered container for all buttons
btn_frame = tk.Frame(frame2, bg=BGCOLOR)
btn_frame.place(relx=0.5, rely=0.6, anchor="center")  # Centered under the display

# Button layout (rows and columns)
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

# Generate all buttons in grid
for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        btn = tk.Button(
            btn_frame,
            text=text,
            font=FONT1,
            width=5,
            height=2,
            bg=BTNCOLOR if text in ("+", "-", "*", "/", "=", "C") else BGCOLOR,
            activebackground="#FFE082",
            command=lambda val=text: on_click(val)
        )
        btn.grid(row=r, column=c, padx=8, pady=8)

# Clear button below the grid
clear_btn = tk.Button(
    btn_frame,
    text="C",
    font=FONT1,
    width=24,
    height=2,
    bg=BTNCOLOR,
    command=lambda: on_click("C")
)
clear_btn.grid(row=4, column=0, columnspan=4, pady=(10, 0))


# ---------------------- MAIN MENU (Frame 1) ----------------------
label = tk.Label(
    frame1,
    text="PIKALKULATOR",
    font=FONT2,
    bg=BGCOLOR,
    fg="black",
)
label.pack(pady=(150, 20))

# Start button with image fallback
try:
    start_img = Image.open("rounded_button.png").resize((200, 60))
    start_img_tk = ImageTk.PhotoImage(start_img)
    start_button = tk.Button(
        frame1,
        image=start_img_tk,
        text="START",
        font=FONTBTN,
        compound="center",
        fg="black",
        bg=BGCOLOR,
        borderwidth=0,
        highlightthickness=0,
        activebackground=BGCOLOR,
        command=lambda: clicked(frame2)
    )
    start_button.image = start_img_tk
    start_button.pack()
except Exception as e:
    print(f"Error loading start button image: {e}")
    start_button = tk.Button(
        frame1,
        text="START",
        font=FONTBTN,
        fg="black",
        bg=BTNCOLOR,
        command=lambda: clicked(frame2)
    )
    start_button.pack()

# Back button (Frame 2)
back_button = tk.Button(
    frame2,
    text="HOME",
    font=FONTBTN,
    fg="black",
    bg=BTNCOLOR,
    command=lambda: clicked(frame1)
)
back_button.place(x=15, y=5)


# Pikachu image (Frame 1)
try:
    pikimg = Image.open("pik.png").resize((400, 400))
    pikimg_tk = ImageTk.PhotoImage(pikimg)
    img_label = tk.Label(frame1, image=pikimg_tk, bg=BGCOLOR)
    img_label.image = pikimg_tk
    img_label.place(relx=0.95, rely=0.55, anchor="e")
except Exception as e:
    print(f"Error loading Pikachu image: {e}")


# ---------------------- START APP ----------------------
frame1.tkraise()
window.mainloop()
