def main():
    inp = input("Expression:")
    x, y, z= inp.split(" ")
    x= float(x)
    z= float(z)
    if y == '+':
        print(x+z)
    elif y == '-':
        print(x-z)
    elif y == '/':
        print(x/z)
    elif y == '*':
        print(x*z)

main()
