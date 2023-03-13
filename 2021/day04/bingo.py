class BingoCard:
    WINNING_STATE = "*****"
    is_complete = False
    
    def __init__(self):
        self.rows = []
    
    def add_row(self, row: str) -> None:
        numbers = [row.strip() for row in row.split(" ")]
        # remove empty strings from list
        self.rows.append(list(filter(None, numbers)))

    def mark_number(self, number: str) -> None:
        for row in self.rows:
            if number in row:
                index = row.index(number)
                row[index] = '*'
    
    def has_won(self) -> bool:
        # check rows first
        for row in self.rows:
            if ''.join(row) == self.WINNING_STATE:
                self.is_complete = True
                return True
        
        # check columns
        for i in range(5):
            if "".join([row[i] for row in self.rows]) == self.WINNING_STATE:
                self.is_complete = True
                return True
            
        return False
    
    def sum_of_remaining_numbers(self) -> int:
        total = 0
        for row in self.rows:
            for number in row:
                if number != "*":
                    total += int(number)
        return total