from searcher import text_search


def extract_words(text: str) -> list[tuple[str, str]]:
    return text_search.search_with_definitions(text)
