
class Question:
    def __init__(self, text: str, options: list, answer: str):
        self.text = text
        self.options = options
        self.answer = answer

    def ask(self) -> None:
        print(self.text)
        i = 1
        for option in self.options:
            print(f'{i}) {option}')
            i += 1
        print(f'{i}) {self.answer}')