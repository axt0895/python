class Author:
    def __init__(self, author_id, author_name, author_publication) -> None:
        self.author_id= author_id
        self.author_name = author_name
        self.author_publication = author_publication

    def __str__(self) -> None:
        print(f'{self.author_id} {self.author_name} {self.author_publication}')
