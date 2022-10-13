class LetterBox:
    def __init__(self, letter=None):
        self.flag_up = False
        self.letter = letter

    def insert_letter(self, letter):
        if self.flag_up:
            print("The flag is up")
        if not self.flag_up:
            self.letter = letter
            self.flag_up = True

    def take_letter(self):
        if not self.flag_up:
            print("You have no letters")
        if self.flag_up:
            self.flag_up = False
            return self.letter




