# cybersecuritycollegecreditcalculator.py
# A calculator that determines how many credits a PTCC Cybersecurity student has until they graduate with a diploma or an AAS.
# By: Noelle Robertson

# Ask the user which program they are pursuing.
cybersecurity_path = input("Are you pursuing the Cyber Security Diploma or the Cyber Security AAS? (type 'Diploma' or 'AAS') ")
AAS_credits = 60
diploma_credits = 45

# If they chose Diploma, ask how many credits they've completed and print how many credits they have left.
if cybersecurity_path == "Diploma":
    diploma_q = eval(input("How many credits have you completed? "))
    diplomacredits_left = diploma_credits - diploma_q
    print("You are pursuing a", cybersecurity_path, "and have", diplomacredits_left, "credits left to graduate.")

# If they chose AAS, ask how many credits they've completed and print how many credits they have left.
if cybersecurity_path == "AAS":
    AAS_q = eval(input("How many credits have you completed? "))
    AAScredits_left = AAS_credits - AAS_q
    print("You are pursuing an", cybersecurity_path, "and have", AAScredits_left, "credits left to graduate.")
