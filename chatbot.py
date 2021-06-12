from enum import Enum, auto
from supermemo2 import SMTwo
from chai_py import ChaiBot, Update

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.review = None

    def update_review(self, quality):
        """ Take the user's input to set the flashcard 'easiness'. """
        quality = int(quality)
        if self.review is None:
            self.review = SMTwo.first_review(quality)
            return self.review
        self.review = self.review.review(quality)
        return self.review

    def __lt__(self, other):
        """ Use the magic 'less-than' method to help us sort the flashcards. """
        if self.review is None:
            return True
        if other.review is None:
            return False
        if self.review.review_date == other.review.review_date:
            return self.review.easiness < other.review.easiness
        return self.review.review_date < other.review.review_date

    def __repr__(self):
        """ Giving our Flashcard a printable output can be helpful
            in the development process. """
        return f"{self.question}, {self.answer}, {self.review}"


class MessageType(Enum):
    QUESTION = auto()
    #ANSWER = auto()
    QUALITY = auto()

class Bot(ChaiBot):
    def setup(self):
        from flashcardSet import flashcardSet
        self.logger.info("Setting up...")
        self.flashcards = flashcardSet
        self.previous_messagetype = None

    async def on_message(self, update: Update) -> str:
        if self.previous_messagetype is MessageType.QUESTION:
            self.previous_messagetype = MessageType.QUALITY
            return f"Answer: {self.flashcards[0].answer}\n\nHow easy was this? (1 - 5)"
        if self.previous_messagetype is MessageType.QUALITY:
            self.flashcards[0].update_review(update.latest_message.text)
            print(self.flashcards[0].review)
            self.flashcards.sort()
        self.previous_messagetype = MessageType.QUESTION
        return self.flashcards[0].question

if __name__=="__main__":
    from chai_py import TRoom
    troom = TRoom([Bot()])
    troom.chat()