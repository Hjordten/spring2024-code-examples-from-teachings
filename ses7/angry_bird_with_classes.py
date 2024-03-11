import random

class Bird:
    def __init__(self):
        self.position = random.randint(1, 10)
        self.direction = 'right'  # Initial direction

    def turn_left(self):
        print("Bird turned left.")
        self.direction = 'left'

    def turn_right(self):
        print("Bird turned right.")
        self.direction = 'right'

    def move_forward(self):
        print(f"Bird moved forward facing {self.direction}.")
        if self.direction == 'right':
            self.position += 1
        else:
            self.position -= 1

        # Wrap around at the grid boundaries
        if self.position > 10:
            self.position = 1
        elif self.position < 1:
            self.position = 10

class Pig:
    def __init__(self):
        self.position = random.randint(1, 10)

class Workspace:
    def __init__(self):
        pass

    def display(self):
        print("Welcome to the Angry Birds Game!")
        print("Instructions:")
        print("q = Quit game")
        print("l = Turn bird left")
        print("r = Turn bird right")
        print("f = Move bird forward")

    def get_user_commands(self):
        command = input("Enter your command: ")
        return command.lower()

class Game:
    def __init__(self):
        self.bird = Bird()
        self.pig = Pig()
        self.workspace = Workspace()

    def run(self):
        self.workspace.display()

        while True:
            print(f"Bird position: {self.bird.position}")
            print(f"Pig position: {self.pig.position}")
            print(f"Bird direction: {self.bird.direction}")

            user_command = self.workspace.get_user_commands()

            if user_command == 'q':
                print("Quitting the game.")
                break
            elif user_command == 'l':
                self.bird.turn_left()
            elif user_command == 'r':
                self.bird.turn_right()
            elif user_command == 'f':
                self.bird.move_forward()
            else:
                print("Invalid command. Please try again.")

            if self.bird.position == self.pig.position:
                print("Congratulations! The bird caught the pig!")
                break

# Example usage:
game = Game()
game.run()
