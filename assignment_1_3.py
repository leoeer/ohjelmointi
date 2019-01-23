onepoint = 1600 / 60
print("One credit point corresponds to", onepoint, "hours of work.")
hours = 1600 // 60
minutes = 1600 % 60
print("This corresponds to", hours, "hours and", minutes, "minutes.")

howmany = int(input("How many credit points is your course? "))
onepoint = round(onepoint / 0.0166666667)
totalhours = int(howmany * onepoint) // 60
totalminutes = int(howmany * onepoint) % 60
print("You need to work", totalhours, "hours and", totalminutes, "minutes to complete your course.")

weeks = int(input("How many weeks does your course take? "))
workh_in_week = totalhours // weeks
workm_in_week = totalminutes % weeks
print("You need to work", workh_in_week, "hours and", workm_in_week, "minutes a week for your course.")








