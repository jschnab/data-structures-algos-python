from turtle import RawTurtle

HUMAN = -1
COMPUTER = 1


class Board:
    def __init__(self, board=None):
        self.items = []
        for i in range(3):
            row = []
            for j in range(3):
                if board is None:
                    row.append(Dummy())
                else:
                    row.append(board[i][j])
           self.items.append(row)

    def __getitem__(self, index):
        """Return a row of the board."""
        return self.items[index]

    def __eq__(self, other):
        """Return True if self and other represent the same state."""
        pass

    def reset(self):
        """
        Mutate the board to contain all dummy turtles.
        Should be used to start a new game.
        """
        screen.tracer(1)
        for i in range(3):
            for j in range(3):
                self.items[i][j].goto(-100, -100)
                self.items[i][j] = Dummy()
        screen.tracer(0)

    def eval(self):
        """
        Return integer representing the state of the game.
        Computer won: 1
        Human won: -1
        Draw: 0
        """
        pass

    def full(self):
        """Return True if the board is filled with Dummy turtles."""
        pass

    def draw(self):
        """Draw the Xs and Os of the board on the screen."""
        for row in range(3):
            for col in range(3):
                if self[row][col].eval() != 0:
                    self[row][col].st()
                    self[row][col].goto(
                        col * 100 + 50,
                        row * 100 + 50
                    )
        screen.update()


class Dummy:
    def __init__(self):
        pass

    def eval(self):
        return 0

    def goto(self, x, y):
        pass


class X(RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.ht()
        self.getscreen().register_shape(
            "X",
            (
                (-40, -36),
                (-40, -44),
                (0, -4),
                (40, -44),
                (40, -36),
                (4, 0),
                (40, 36),
                (40, 44),
                (0, 4),
                (-40, 44),
                (-40, 36),
                (-4, 0),
                (-40, -36),
            )
        )
        self.shape("X")
        self.penup()
        self.speed(5)
        self.goto(-100, -100)

    def eval(self):
        return COMPUTER


class O(RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.ht()
        self.shape("circle")
        self.penup()
        self.speed(5)
        self.goto(-100, -100)

    def eval(self):
        return HUMAN
