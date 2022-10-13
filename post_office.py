class PostOffice:
    def __init__(self, letter=None):
        self.contains_letter = False
        self.letter = letter

    def give_letter(self, letter):
        if self.contains_letter:
            print("sorry we already hold a letter")
        if not self.contains_letter:
            self.contains_letter = True
            self.letter = letter

    def take_letter(self):
        if not self.contains_letter:
            print("No Letter to retrieve")
        if self.contains_letter:
            self.contains_letter = False
            return self.letter
