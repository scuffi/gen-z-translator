from ..searcher import text_search


def add_word_command(ack, command, respond):
    ack()
    word, definition = command["text"].split(" ", maxsplit=1)
    text_search._database.add_word(word, definition)
    respond(f"Added {word} with definition {definition} to database")


def remove_word_command(ack, command, respond):
    ack()
    word = command["text"]
    text_search._database.remove_word(word)
    respond(f"Removed {word} from database")


def update_definition_command(ack, command, respond):
    ack()
    word, definition = command["text"].split(" ", maxsplit=1)
    text_search._database.update_definition(word, definition)
    respond(f"Updated definition of {word} to {definition}")
