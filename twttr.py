inp = input("Input:")
print(inp.translate({ord(i): None for i in 'aiueoAIUEO'}))
