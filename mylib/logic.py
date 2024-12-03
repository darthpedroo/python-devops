import wikipedia


def wiki(name="Fanta Cake", length=1):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)

    return my_wiki
