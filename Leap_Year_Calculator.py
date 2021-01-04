# 🚨 Don't change the code below 👇
jahr = int(input("Which jahr do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if jahr % 4 == 0 and jahr % 100 != 0:
    print("Schaltjahr.")
elif jahr % 4 == 0 and jahr % 100 == 0:
    if jahr % 400 == 0:
        print("Schaltjahr.")
    else:
        print("Kein Schaltjahr.")
else:
    print("Kein Schaltjahr.")