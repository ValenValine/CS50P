def main():
    time= input("Time:")
    sum = convert(time)
    if (sum >= 7.0) and (sum <= 8.0):
        print("breakfast time")
    elif (sum >= 12.0) and (sum <= 13.0):
        print("lunch time")
    elif (sum >= 18.0) and (sum <= 19.0):
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    min = float(minutes)
    minutes = min/60.0
    sum = hours + minutes
    return sum


if __name__ == "__main__":
    main()
