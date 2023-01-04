import webbrowser

def search():
    term = input("TERMO: ")
    where = input("ONDE: ")

    if where == "navegador" or where == "browser" or where == "google" or where == "g":
        webbrowser.open("https://www.google.com/search?q="+term)
    elif where == "bing" or where == "b":
        webbrowser.open("https://www.bing.com/search?q="+term)
    elif where == "duck" or where == "duckduck" or where == "duckduckgo" or where == "d":
        webbrowser.open("https://duckduckgo.com/?q="+term)
    elif where == "wikipedia" or where == "wiki" or where == "w":
        webbrowser.open("https://pt.wikipedia.org/wiki/"+term)
    elif where == "stackoverflow" or where == "stack" or where == "s":
        webbrowser.open("https://pt.stackoverflow.com/search?q="+term)
    elif where == "github" or where == "git":
        webbrowser.open("https://github.com/search?q="+term)
    elif where == "youtube" or where == "y":
        webbrowser.open("https://www.youtube.com/results?search_query="+term)
    else:
        print("Não consegui encontrar, senhor.")
