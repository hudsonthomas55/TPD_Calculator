from tkinter import *

# ---------------------------------------------- WINDOW SETUP ---------------------------------------------- #
window = Tk()
window.minsize(width=500, height=500)
window.title("TPD Calculator")
window.config(padx=50, pady=50)


# -------------------------------------------- FUNCTIONS---------------------------------------- #
def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()


# -------------------------------------------- CODE ---------------------------------------- #
aww = input("Enter pre-injury AWW (no commas): \n$")
date_from = input("Enter starting date (MM/DD/YY): \n")
date_to = input("Enter ending date (MM/DD/YY): \n")
earnings = input("How much were the earnings during this period? \n$")


tpd_owed = round((float(aww) - float(earnings)) * 0.6667, 2)

message = f"TPD calculated for period from {date_from} to {date_to}, pre-injury AWW is ${aww}, earnings during this " \
          f"period was {earnings}. ${tpd_owed} is owed."

print(f"TPD owed: {tpd_owed}. Copy/paste below message:")
print(message)


def main_screen():
    clear_frame()
    welcome_label = Label(text="Welcome! \n Let's calculate some TPD. \n", font=("Arial", 30))
    welcome_label.grid(row=0, column=0, columnspan=3)


# ---------------------------------------- KEEP WINDOW OPEN ---------------------------------------- #
main_screen()
window.mainloop()


