import wikipediaapi
import wikipedia
from yake import KeywordExtractor

wiki = wikipediaapi.Wikipedia(
    user_agent="masoncute4real@gmail.com",
    language="en",
)


def get_wiki_summary(title):
    """Return the summary of a Wikipedia page, or None if it doesn't exist."""
    page = wiki.page(title)
    if not page.exists():
        return None
    return page.summary



def search_wiki_pages(query, results=5):
    """Return a list of page titles matching the query."""
    return wikipedia.search(query, results=results)

# build a function to return the wikipedia page
def get_wiki_page(page):
    """Return a Wikipedia page, or None if it doesn't exist."""
    page = wiki.page(page)
    if not page.exists():
        return None
    return page

# return the keywords of a wikipedia page
def get_wiki_keywords(page, max_keywords=10):
    """Return a list of keywords for a Wikipedia page."""
    page = get_wiki_page(page)
    if not page:
        return None
    text = page.text
    kw_extractor = KeywordExtractor()
    keywords = kw_extractor.extract_keywords(text)
    return [kw[0] for kw in keywords[:max_keywords]]