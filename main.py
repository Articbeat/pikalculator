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
window.geometry("600x500")  # ✅ Add default window size for better layout


# ---------------------- FRAMES ----------------------
frame1 = tk.Frame(window, bg=BGCOLOR)
frame1.place(relwidth=1, relheight=1)

frame2 = tk.Frame(window, bg=BGCOLOR)
frame2.place(relwidth=1, relheight=1)


# ---------------------- CALCULATOR (Frame 2) ----------------------
calc_display = tk.Entry(
    frame2,
    font=("Arial", 24),
    justify="right",
    relief="solid",
    bd=2
)
calc_display.place(relx=0.5, y=60, width=400, height=50, anchor="center")

buttons = [
    ("7", 100, 150), ("8", 180, 150), ("9", 260, 150), ("/", 340, 150),
    ("4", 100, 220), ("5", 180, 220), ("6", 260, 220), ("*", 340, 220),
    ("1", 100, 290), ("2", 180, 290), ("3", 260, 290), ("-", 340, 290),
    ("0", 100, 360), (".", 180, 360), ("=", 260, 360), ("+", 340, 360),
    ("C", 100, 430)
]

for text, x, y in buttons:
    btn = tk.Button(
        frame2,
        text=text,
        font=FONT1,
        width=5 if text != "C" else 22,
        height=2,
        bg=BTNCOLOR if text in ("+", "-", "*", "/", "=", "C") else BGCOLOR,  # ✅ Better contrast
        activebackground="#FFE082",
        command=lambda val=text: on_click(val)
    )
    btn.place(x=x, y=y)


# ---------------------- MAIN MENU (Frame 1) ----------------------
label = tk.Label(
    frame1,
    text="PIKALKULATOR",
    font=FONT2,
    bg=BGCOLOR,
    fg="black",
)
label.pack(pady=(150, 20))

# ✅ Start button with fallback if image missing
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


# ✅ Back button (Frame 2)
back_button = tk.Button(
    frame2,
    text="HOME",
    font=FONTBTN,
    fg="black",
    bg=BTNCOLOR,
    command=lambda: clicked(frame1)
)
back_button.place(x=15, y=5)


# ✅ Pikachu image on main menu
try:
    pikimg = Image.open("pik.png").resize((400, 400))
    pikimg_tk = ImageTk.PhotoImage(pikimg)
    img_label = tk.Label(frame1, image=pikimg_tk, bg=BGCOLOR)
    img_label.image = pikimg_tk
    img_label.place(relx=0.95, rely=0.55, anchor="e")  # ✅ Better alignment
except Exception as e:
    print(f"Error loading Pikachu image: {e}")


# ---------------------- DEFAULT FRAME ----------------------
frame1.tkraise()
window.mainloop()
