from letter import Letter
from post_office import PostOffice
class Alice:
    def __init__(self, letter_box, letter=None):
        self.letter_box = letter_box
        self.letter = letter

    def send_letter(self, destination, message, post_office):
        letter = Letter(message, destination)
        Letter.write_letter(letter, message, destination)
        PostOffice.give_letter(post_office, letter)
        print("Letter sent to post office")

    def get_letter(self, destination):
        print("checking Mailbox")
        if not destination.flag_up:
            print("You have no mail!")
        if destination.flag_up:
            print("You've got mail!")
            self.letter = destination.take_letter()
            self.letter.read_letter()
