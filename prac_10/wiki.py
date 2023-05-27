import wikipedia
ask = input("Enter a searching: ")
while ask != "":
    ask = wikipedia.page(ask, auto_suggest=False)
    print(ask.title)
    print(ask.url)
    print(ask.summary)
    ask = input("Enter a searching: ")


