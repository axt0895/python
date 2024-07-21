class Publisher:
    def __init__(self, publisher_id, publisher_name) -> None:
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name
        
    def __str__(self) -> None:
        print(f'{self.publisher_id} & {self.publisher_name}')