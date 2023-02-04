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


# -------------------------------------------- OLD CODE ---------------------------------------- #
# aww = input("Enter pre-injury AWW (no commas): \n$")
# date_from = input("Enter starting date (MM/DD/YY): \n")
# date_to = input("Enter ending date (MM/DD/YY): \n")
# earnings = input("How much were the earnings during this period? \n$")
#
#
# tpd_owed = round((float(aww) - float(earnings)) * 0.6667, 2)
#
# message = f"TPD calculated for period from {date_from} to {date_to}, pre-injury AWW is ${aww}, earnings during this " \
#           f"period was {earnings}. ${tpd_owed} is owed."

# print(f"TPD owed: {tpd_owed}. Copy/paste below message:")
# print(message)

# ------------------------------------- MAIN SCREEN ------------------------------------- #
def main_screen():
    clear_frame()

    # SUBMIT BUTTON
    def submit_button():
        print("the button works")


    welcome_label = Label(text="Welcome! \n Let's calculate some TPD. \n\n", font=("Arial", 30))
    welcome_label.grid(row=0, column=0, columnspan=3)

    # AWW Section
    aww_label = Label(text="Enter the pre-injury average weekly wage: ")
    aww_label.grid(row=1, column=0)
    aww_entry = Entry(width=30)
    aww_entry.insert(END, string="Do not include special characters ('$' or ',')")
    aww_entry.grid(row=1, column=1, columnspan=3)

    # Date Section
    date_label = Label(text="Enter the date range: ")
    date_label.grid(row=2, column=0)
    date_from_entry = Entry(width=13)
    date_from_entry.insert(END, string="MM/DD/YY")
    date_from_entry.grid(row=2, column=1)
    dash_label = Label(text="-")
    dash_label.grid(row=2, column=2)
    date_to_entry = Entry(width=13)
    date_to_entry.insert(END, string="MM/DD/YY")
    date_to_entry.grid(row=2, column=3)

    # Earnings Section
    earnings_label = Label(text="How much did the employee earn during this period? ")
    earnings_label.grid(row=3, column=0)
    earnings_entry = Entry(width=30)
    earnings_entry.insert(END, string="Do not include special characters ('$' or ',')")
    earnings_entry.grid(row=3, column=1, columnspan=3)

    # Submit Button
    spacer_label = Label(text="\n")
    spacer_label.grid(row=4, column=0)
    submit_button = Button(text="Calculate TPD", width=30, command=submit_button)
    submit_button.grid(row=5, column=0, columnspan=2)


# ---------------------------------------- KEEP WINDOW OPEN ---------------------------------------- #
main_screen()
window.mainloop()


