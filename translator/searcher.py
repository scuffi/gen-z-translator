from textsearch import TextSearch


class TextSearcher:
    def __init__(self):
        self._searcher = TextSearch("ignore", "norm")

    def search(self, text: str):
        return self._searcher.findall(text)
