class Deck:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = ['A', 'K', 4, 7]
        else:
            self.cards = cards

    def __getitem__(self, key): # Using [<postitional argument(s)] will call this built-in function
        return self.cards[key]

    def __repr__(self): # Using repr(<Deck object>) will call this built-in function
        return f'Deck({self.cards})'

    def __len__(self): # Using len(<Deck object>) will call this built-in function
        return len(self.cards)
    
    def __add__(self, other): # Using + operator will call this built-in function
       #return Deck(self.cards + other.cards)
        d = Deck()
        d.cards = self.cards + other.cards

    def __str__(self): # Using print() will call this built-in function
        return ', '.join(map(str, self.cards))  # Join cards into a string separated by commas

    def __setitem__(self, key, value): # Using assignment statement will call this built-in function
        self.cards[key] = value  # Update value at the given index

    def __delitem__(self, key): # Using del statement will call this built-in function
        del self.cards[key]  # Delete item at the given index
