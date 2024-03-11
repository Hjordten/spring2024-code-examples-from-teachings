class Game:
    def __init__(self):
        self.board = [['*'] * 10 for _ in range(10)]
        self.bird = {'x': 2, 'y': 2, 'direction': 'right'}
        self.pig = {'x': 8, 'y': 8}

    def display(self):
        for row in self.board:
            print(' '.join(row))

    def move_bird(self, command):
        if command == 'f':
            if self.bird['direction'] == 'right':
                self.bird['x'] += 1
            else:
                self.bird['x'] -= 1
        elif command == 'l':
            self.bird['direction'] = 'left'
        elif command == 'r':
            self.bird['direction'] = 'right'

    def check_win_or_lose(self):
        if self.bird['x'] == self.pig['x'] and self.bird['y'] == self.pig['y']:
            print("Bird won the game!")
            return True
        else:
            print("Bird lost the game.")
            return False

    def run(self):
        self.display()
        while True:
            command = input("Enter command (f, l, r, q): ").lower()
            if command == 'q':
                break
            self.move_bird(command)
            self.display()
            if self.check_win_or_lose():
                break

if __name__ == "__main__":
    game = Game()
    game.run()
