import wikipedia

ask = input("Enter what you want to search: ")
while ask != "":
    try:
        ask_page = wikipedia.page(ask, autosuggest=False)
        print(ask_page.title)
        print(ask_page.url)
        print(ask_page.summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)