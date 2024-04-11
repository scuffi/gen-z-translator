from database import WordDatabase
from textsearch import TextSearch


class TextSearcher:
    def __init__(self):
        self._searcher = TextSearch("ignore", "norm")
        self._database = WordDatabase()

        self._add_definitions()

    def _add_definitions(self):
        self._searcher.add([doc["word"] for doc in self._database.get_words()])

    def search(self, text: str):
        return self._searcher.findall(text)

    def search_with_definitions(self, text: str):
        words = self.search(text)

        return list(
            filter(
                None,
                (
                    (word, self._database.get_word(word)["definition"])
                    if self._database.get_word(word)
                    else None
                    for word in words
                ),
            )
        )


text_search = TextSearcher()
