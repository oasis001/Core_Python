import datetime

print("Hello there!!!! Its a survey of the people")

name = input("Hey Mr/Miss whats your name?")

age = int(input("okay cool than how old are you?"))

date = int(datetime.date.today().strftime("%Y"))

print("so hey " + name + " you will be " + str((date-age)+100) + " after 100 years")
