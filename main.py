aww = input("Enter pre-injury AWW (no commas): \n$")
date_from = input("Enter starting date (MM/DD/YY): \n")
date_to = input("Enter ending date (MM/DD/YY): \n")
earnings = input("How much were the earnings during this period? \n$")


tpd_owed = round((float(aww) - float(earnings)) * 0.6667, 2)

message = f"TPD calculated for period from {date_from} to {date_to}, pre-injury AWW is ${aww}, earnings during this " \
          f"period was {earnings}. ${tpd_owed} is owed."

print(f"TPD owed: {tpd_owed}. Copy/paste below message:")
print(message)




