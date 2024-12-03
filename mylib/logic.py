import wikipedia


def wiki(name:str, length=1):
    """This is a wikipedia fetcher"""    
    try:
        result = search_wiki(name)
        print("result", result)
        first_result = result[0]
        my_wiki = wikipedia.summary(first_result, length)
        return my_wiki
    except Exception as ex:
        print("Error:", ex)

def search_wiki(query: str):
    """Search Wikipedia for Names"""
    results = wikipedia.search(query)
    return results
