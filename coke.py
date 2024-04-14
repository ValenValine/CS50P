def amount_due():
    due = 50
    while due > 0:
        coin = int(input("Insert coin:"))
        if coin > due:
            owed = coin - due
            due = 0
            print(f"Change Owed: {owed}")
            return due
        else:
            if coin == 25:
                due = due - 25
                print(f"Amount Due: {due}")
            elif coin == 10:
                due = due - 10
                print(f"Amount Due: {due}")
            elif coin == 5:
                due = due - 5
                print(f"Amount Due: {due}")
            else:
                print(f"Amount Due: {due}")
    else:
        print("Change Owed: 0")

amount_due()
