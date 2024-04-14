inp = input("Input:")
print(inp.translate({ord(i): '_' +i.lower() for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}))
