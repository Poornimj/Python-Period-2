class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name, end=" ")


class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_info(self):
        super().print_info()
        print("(author" + self.author + " " + str(self.pages) + "pages)")


class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        super().print_info()
        print("editor" + self.editor)


pub = []
pub.append(Magazine("Donald Duck", "Aki Hyppa"))
pub.append(Book("Compartment No.6", "Rosa Likson", 192))
for i in pub:
    i.print_info()
