def main():
    answer = input("What is your answer to the Great Question of Life, the Universe, and Everything?").lower().strip()
    if answer == "42":
        print("Yes")
    elif answer == "forty-two":
        print("Yes")
    elif answer == "forty two":
        print("Yes")
    else:
        print("No")

main()