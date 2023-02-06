from tkinter import *

# ---------------------------------------------- WINDOW SETUP ---------------------------------------------- #
window = Tk()
window.minsize(width=500, height=500)
window.title("TPD Calculator")
window.config(padx=50, pady=50)

# -------------------------------------------- REFERENCES ---------------------------------------- #
aww = 0
date_from = ""
date_to = ""
earnings = 0


# -------------------------------------------- FUNCTIONS---------------------------------------- #
def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()




# ------------------------------------- MAIN SCREEN ------------------------------------- #
def main_screen():
    clear_frame()

    # Submit button function
    def submit_button():
        global aww
        global date_from
        global date_to
        global earnings

        # Get user inputs
        aww_answer = aww_entry.get()
        date_from_answer = date_from_entry.get()
        date_to_answer = date_to_entry.get()
        earnings_answer = earnings_entry.get()

        # Update global variables
        aww = aww_answer.replace("$", "").replace(",", "")
        date_from = date_from_answer
        date_to = date_to_answer
        earnings = earnings_answer.replace("$", "").replace(",", "")

        # Run TPD calculation based on user inputs
        tpd_calc()

    def tpd_calc():
        tpd_owed = ((float(aww) - float(earnings)) * .6667)
        tpd_rounded = round(tpd_owed, 2)
        return_label.config(text=f"TPD calculated for date range: {date_from}-{date_to}. \n"
                                 f"AWW was ${aww}, earnings were ${earnings}. \n"
                                 f"TPD owed for this period is ${tpd_owed}. \n"
                                 f"TPD paid is: ${tpd_rounded}. \n")

    # Screen setup
    welcome_label = Label(text="Welcome! \n Let's calculate some TPD. \n\n", font=("Arial", 30))
    welcome_label.grid(row=0, column=0, columnspan=3)

    # AWW Section
    aww_label = Label(text="Enter the pre-injury average weekly wage: ")
    aww_label.grid(row=1, column=0)
    aww_entry = Entry(width=30)
    aww_entry.insert(END, string="$1,000")
    aww_entry.grid(row=1, column=1, columnspan=3)
    aww_entry.focus_set()

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
    earnings_entry.insert(END, string="$500")
    earnings_entry.grid(row=3, column=1, columnspan=3)

    # Submit Button
    spacer_label = Label(text="\n\n")
    spacer_label.grid(row=4, column=0)
    return_label = Label(text="", justify=LEFT, anchor="w")
    return_label.grid(row=5, column=0, columnspan=4)
    submit_button = Button(text="Calculate TPD", width=30, command=submit_button)
    submit_button.grid(row=6, column=0, columnspan=2)


# ---------------------------------------- KEEP WINDOW OPEN ---------------------------------------- #
main_screen()
window.mainloop()


