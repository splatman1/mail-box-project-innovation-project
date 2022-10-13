from letter_box import LetterBox
from alice import Alice
from bob import Bob
from charlie import Charlie
from post_office import PostOffice
from letter import Letter

alice_letter_box = LetterBox()
bob_letter_box = LetterBox()
bob = Bob(bob_letter_box)
alice = Alice(alice_letter_box)
post_office = PostOffice()
charlie = Charlie()
letter = Letter()

alice.send_letter(bob_letter_box, " Bob ", post_office)
charlie.collect_letter(post_office)
charlie.check_flag_position(bob_letter_box)
charlie.deliver_letter(bob_letter_box)
bob.get_letter(bob_letter_box)
print("\n")
bob.send_letter(alice_letter_box, " Alice", post_office)
charlie.collect_letter(post_office)
charlie.check_flag_position(alice_letter_box)
charlie.deliver_letter(alice_letter_box)
alice.get_letter(alice_letter_box)


