class Movies:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

    def print_title(self):
        print(f"\n{self.title} was release in {self.year}, and currently has a score of {self.rating}.")


inception = Movies("Inception", 2010, 8.8)
the_martian = Movies("The Martial", 2015, 8.0)
joker = Movies("Joker", 2019, 8.4)

print(f"\n{inception.title} was release in {inception.year}, and currently has a score of {inception.rating}.")

inception.print_title()
the_martian.print_title()
joker.print_title()
