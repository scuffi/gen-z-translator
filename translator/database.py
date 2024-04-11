from tinydb import Query, TinyDB


class WordDatabase:
    # TODO: Add alias' for words, pointing to a single definition
    def __init__(self):
        self.db = TinyDB("words.json")

    def add_word(self, word: str, definition: str):
        self.db.insert({"word": word, definition: definition})

    def remove_word(self, word: str):
        self.db.remove(Query().word == word)

    def update_definition(self, word: str, definition: str):
        self.db.update({"definition": definition}, Query().word == word)

    def get_words(self):
        return self.db.all()
