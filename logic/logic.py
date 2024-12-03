import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError
from textblob import TextBlob
import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("omw-1.4")


def wiki(name: str, length=1):
    """This is a wikipedia fetcher"""
    try:
        result = search_wiki(name)
        first_result = result[0]
        print(first_result)
        print("HOLA")
        my_wiki = wikipedia.summary(first_result, length)
        return my_wiki
    except DisambiguationError as de:
        print("Disambiguation error:", de)
    except PageError as pe:
        print("Page not found error:", pe)
    except IndexError:
        print("No results found for the search query.")


def search_wiki(query: str):
    """Search Wikipedia for Names"""
    results = wikipedia.search(query)
    return results


def phrase(query: str):
    """Returns phrases from wikipedia"""
    page = wiki(query)
    blob = TextBlob(page)
    return blob.noun_phrases
