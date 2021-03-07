import random
from string import *
from tkinter import *
from tkinter import messagebox
import pyperclip
####
# -----------------------------------------------#
# ------------------UI SETUP---------------------#
# -----------------------------------------------#
###
# Window Configuration
window = Tk()
window.title('Password Generator and Manager')
window.config(padx=70, pady=40)

# Canvas Management
canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="keepass-password-safe-logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_entry = Entry(text="", width=55)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(text="", width=55)
email_entry.insert(0, "sumeetagrawal840@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(text="", width=37)
password_entry.grid(column=1, row=3)


def generate_random_password():
    if not len(website_entry.get()):
        password_entry.delete(0, END)
        messagebox.showerror(title="Empty Field ",message="Invalid option. Either Website or Password field is empty.")
    ##Random Password Method 1
    else:
        random_punc = [punctuation[random.randint(0,len(punctuation)-1)] for i in range(2)]
        random_uppercase = [ascii_uppercase[random.randint(0,len(ascii_uppercase)-1)] for i in range(9)]
        random_digits = [digits[random.randint(0,len(digits)-1)] for i in range(1)]
        all_characters = random_punc + random_uppercase + random_digits
        output = ''.join(random.sample(all_characters, 12))
        ##Random Password Method 2
        # all_characters = punctuation + ascii_letters + digits
        # output = ''.join(random.sample(all_characters,12))
        password_entry.delete(0, END)
        password_entry.insert(0, output)
        pyperclip.copy(output)

generate_password = Button(text="Generate Password", command=generate_random_password)
generate_password.grid(column=2, row=3)

def add_details_to_file():
    website = website_entry.get()
    is_ok = messagebox.askyesno(title=f"{website}", message="Are you good to save these?")
    if is_ok:
        with open('filenme.txt', 'a') as file:
            file.write(f"{website},{email_entry.get()},{password_entry.get()}\n")

add_button = Button(text="Add", width=47, command=add_details_to_file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
