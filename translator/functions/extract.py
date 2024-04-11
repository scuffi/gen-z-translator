from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..searcher import TextSearcher


def extract_words(text: str, searcher: TextSearcher) -> list[str]:
    return searcher.search_with_definitions(text)
