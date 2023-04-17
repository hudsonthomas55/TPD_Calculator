# TPD_Calculator
Calculates Temporary Partial Disability payments under workers' compensation - for insurance adjusters



As an insurance adjuster, I calculate TPD payments on a weekly basis. This calculator takes some of the headache away, and saves repetitive typing. Prior 
to using this calculator, I would have to do the calculations and then type a message out explaining the calculations... essentially doing it twice.
All you have to do to use this program is put in the starting amount, date range, and earnings during the period. 
This calculator does the math for you, and even prints a note you can paste into your claim file - now with the use of the Pyperclip python module, this 
program automatically copies the note into the user's clipboard so that it is easier to paste into the file.


Important note, this follows TN specific TPD regulations. NC and AL are similar but adjusters must verify the regulations are similar. 
Additionally, if earnings are higher than the AWW, the return value from this program is negative. Nothing would be owed in this instance (under TN).
