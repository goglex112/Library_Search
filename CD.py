from Main import LibraryItem

class Cd(LibraryItem):
    def __init__(self, title, upc, subject, artist):
        LibraryItem.__init__(self, title, upc, subject)
        self.actors = artist
        self.type = "CD"