from post_office import PostOffice


class Charlie:
    def __init__(self, letter=None):
        self.letter = letter

    def collect_letter(self, post_office):
        self.letter = PostOffice.take_letter(post_office)
    def check_flag_position(self, destination):
        if destination.flag_up:
            print("This letter box already contains a letter")
        if not destination.flag_up:
            pass

    def deliver_letter(self, destination):
        destination.insert_letter(self.letter)

