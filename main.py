import tkinter as tk
import tkinter.ttk as ttk
import time
from generator import generate_password
from strength import strength_calculator
from utilities import clipboard, save_file

# Initialise and set the main screen of tkinter
root = tk.Tk()
root.geometry("1000x600")
bg_color = "#%02x%02x%02x" % (200, 240, 240)

# Set title and background of window
root.title("Password Generator")
icon = tk.PhotoImage(file="images/icon.png")
root.iconphoto(True, icon)
root.config(background=bg_color)

# Defining variables
password_len = tk.StringVar()
password_len.set(value=12)

password = tk.StringVar()
password.set("")

selected_option = tk.StringVar()
menu = tk.Menu(root, tearoff=0)

upper = tk.IntVar(value=1)
lower = tk.IntVar(value=1)
digit = tk.IntVar(value=0)
punctuation = tk.IntVar(value=0)

error_text = ""
strength_text = ""
options = ["Your Passwords"]

# Defining the style
ui_style = ttk.Style()
ui_style.configure(
    "TCheckbutton",
    foreground="black",
    background=bg_color,
)
ui_style.configure(
    "TButton",
    foreground="black",
    background=bg_color,
)
ui_style.configure("TEntry", background=bg_color)
ui_font = "berlinsansfbdemi 10"
# ui_font = "georgia 15 roman"
# ui_font = "sthupo 12 roman"


# Defining functions
def fun():
    global password, error_text, strength_text, options
    try:
        int(password_len.get())
        ent_password.delete(0, tk.END)
        password = generate_password(
            int(password_len.get()),
            upper.get(),
            lower.get(),
            digit.get(),
            punctuation.get(),
        )

        ent_password.insert(0, password)
        options.append(password)
        update_option_menu()
        strenght(password)

    except ValueError:
        error_text = "Please enter a valid password length"
    lbl_error.config(text=error_text, foreground=bg_color)


def strenght(password):
    global error_text, strength_calculator
    error_text = ""
    strength = strength_calculator(password)
    if strength >= 5.0:
        lbl_strength.config(text="Password is very strong", foreground="green")
    if strength > 3.0 and strength < 5.0:
        lbl_strength.config(text="Password is strong", foreground="blue")
    if strength <= 3.0:
        lbl_strength.config(
            text="Password is weak, please choose another password",
            foreground=bg_color,
        )


def update_option_menu():
    if len(options) > 15:
        options.pop(0)
    menu.delete(0, tk.END)
    for option in options:
        menu.add_command(
            label=str(option),
            command=lambda opt=f"{options.index(option)+1}. {option}": selected_option.set(
                opt
            ),
        )
    optionbox_password_history["menu"] = menu


# Code for histry box
def update_pass_box(*args):
    selected = selected_option.get()
    ent_password.delete(0, tk.END)
    ent_password.insert(0, selected)
    strenght(selected)


# Defining frames
frm_1 = tk.Frame(background=bg_color)
frm_2 = tk.Frame(background=bg_color)
frm_3 = tk.Frame(width=150, background=bg_color)
frm_4 = tk.Frame(width=150, background=bg_color)
frm_5 = tk.Frame(width=150, background=bg_color)
frm_6 = tk.Frame(width=150, background=bg_color)
frm_7 = tk.Frame(background=bg_color)
frm_8 = tk.Frame(background=bg_color)
frm_9 = tk.Frame(background=bg_color)
frm_10 = tk.Frame(background=bg_color)
frm_11 = tk.Frame(background=bg_color)


# Defining widgets
lbl_title = ttk.Label(
    master=frm_1, text="Password Generator", background=bg_color, font="forte 35"
)

lbl_password_len = ttk.Label(
    master=frm_2,
    text="Enter the length of the password",
    background=bg_color,
    font=ui_font,
)
ent_password_len = ttk.Entry(
    master=frm_2, width=30, textvariable=password_len, background=bg_color
)

chk_upper = ttk.Checkbutton(
    master=frm_3,
    text="Include Uppercase letters",
    variable=upper,
    onvalue=1,
    offvalue=0,
)

chk_lower = ttk.Checkbutton(
    master=frm_4,
    text="Include Lowercase letters",
    variable=lower,
    onvalue=1,
    offvalue=0,
)

chk_digit = ttk.Checkbutton(
    master=frm_5, text="Include Digits", variable=digit, onvalue=1, offvalue=0
)

chk_special = ttk.Checkbutton(
    master=frm_6,
    text="Include Special characters",
    variable=punctuation,
    onvalue=1,
    offvalue=0,
)

btn_generate = ttk.Button(master=frm_7, text="Generate Password", command=fun)

lbl_password = ttk.Label(
    master=frm_8, text="Your Password", background=bg_color, font=ui_font
)
ent_password = ttk.Entry(
    master=frm_8, width=30, textvariable=password, background=bg_color
)
btn_copy = ttk.Button(
    master=frm_8,
    text="Copy Password",
    command=lambda: clipboard(lbl_error, root, ent_password.get()),
)
btn_save = ttk.Button(
    master=frm_8,
    text="Save Password",
    command=lambda: save_file(
        f'Your password saved at {time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(time.time()))} is {password}'
    ),
)

lbl_strength = ttk.Label(
    master=frm_9, text=strength_text, background=bg_color, font=ui_font
)

lbl_error = ttk.Label(master=frm_10, text=error_text, background=bg_color)

lbl_password_history = ttk.Label(
    master=frm_11, text="Past Passwords", background=bg_color, font=ui_font
)
optionbox_password_history = ttk.OptionMenu(frm_11, selected_option, *options)

# Packing widgets
frm_1.pack(pady=10)
lbl_title.pack(side=tk.TOP)

frm_2.pack(pady=20)
lbl_password_len.pack(side=tk.LEFT)
ent_password_len.pack(side=tk.LEFT, padx=5)

frm_3.pack(pady=10)
chk_upper.pack(side=tk.TOP)

frm_4.pack(pady=5)
chk_lower.pack(side=tk.TOP)

frm_5.pack(pady=5)
chk_digit.pack(side=tk.TOP)

frm_6.pack(pady=5)
chk_special.pack(side=tk.TOP)

frm_7.pack(pady=20)
btn_generate.pack(side=tk.TOP)

frm_8.pack(pady=5)
lbl_password.pack(side=tk.LEFT)
ent_password.pack(side=tk.LEFT, padx=5)
btn_copy.pack(side=tk.LEFT, padx=5)
btn_save.pack(side=tk.LEFT, padx=3)

frm_9.pack(pady=10)
lbl_strength.pack(side=tk.TOP)

frm_10.pack(pady=10)
lbl_error.pack()

frm_11.pack(pady=10)
lbl_password_history.pack(side="left")
optionbox_password_history.pack(side="left", padx=5)

# Bind the update_entry_box function to the selected_option variable
selected_option.trace("w", update_pass_box)

# Main loop of tkinter
root.mainloop()
