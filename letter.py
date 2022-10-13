class Letter:
    def __init__(self, message=None, destination=None):
        self.is_read = False
        self.encrypted = False
        self.content = message
        self.destination = destination

    def read_letter(self,):
        self.is_read = True
        self.decrypt_letter()
        print("Decrypting Letter")
        print("Letter Decrypted")
        print(self.content)

    def write_letter(self, message, destination):
        self.content = ("Hello" + message)
        self.encrypt_letter()
        self.destination = destination
        print("Writing Letter")
        print("Letter Written")
        print("Encrypting Letter")
        print("Letter Encrypted")
        return Letter

    def encrypt_letter(self):
        self.encrypted = True

    def decrypt_letter(self):
        self.encrypted = False
