# Asking

while True:
    name = input("Enter your name:  ").upper()
    print("\nHello", name, "How are you?\n")
    fine = input("Are you fine? Enter (Yes/No) :  ").lower()

    while fine not in ("yes", "no"):
        fine = input("Are you fine? Enter (Yes/No) :  ")

    if fine == "yes":
        print("Okaii, Nice to meet you.\n")
    elif fine == "no":
        print("Well, I wish you will get well Soon!!\n")

    ask = None
    while ask not in ("yes", "no"):
        ask = input("Willing to Ask again? (Yes/No): ").lower()

    if ask != "yes":
        break

print("\nOkay, Bye!! Take Care!!")
