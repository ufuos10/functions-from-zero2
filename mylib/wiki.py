import wikipedia-api

# Build a function to return the summary of a wikipedia page

def get_wiki_summary(page):
    """
    Return the summary of a wikipedia page
    """
    return wikipedia.summary(page)

# build a function search wikipedia pages for a match
def search_wiki_pages(page):
    """
    search wikipedia pages for a match
    """
    return wikipedia.search(page)