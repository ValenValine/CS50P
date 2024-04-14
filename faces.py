def main():
    sentence= input("Enter your sentence with emoticons:")
    sentence= convert(sentence)

def convert(sentence):
    return print(sentence.replace(":)", "🙂").replace(":(", "🙁"))

main()
