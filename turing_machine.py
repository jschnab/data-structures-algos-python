class AddingMachine:
    """
    Defines a Turing machine to perform unary addition.
    """
    def __init__(self, tape, verbose=False):
        """
        :param str tape: tape to feed in the turing machine such as
                         '11+111'
        :param bool verbose: whether or not to print explanatory messages
        """
        self.tape = list(tape)
        self.tape.insert(0, "0")
        self.tape.append("0")
        self.length = len(self.tape)
        self.position = 1
        self.verbose = verbose

    def read(self):
        return self.tape[self.position]

    def write(self, symbol):
        self.tape[self.position] = symbol

    def move_left(self):
        self.position -= 1
        if self.position == 0:
            self.tape.insert(0, "0")
            self.length += 1

    def move_right(self):
        self.position += 1
        if self.position == self.length:
            self.tape.append("0")
            self.length += 1

    def start(self):
        self.A()

    def halt(self):
        result = 0
        for i in self.tape[self.position:]:
            if i == "1":
                result += 1
        print(result)

    def halting_error(self):
        raise ValueError("machine halted before program completion")

    def A(self):
        if self.verbose:
            print(f"A, {self.tape}, {self.position}")
        if self.read() == "1":
            self.write("0")
            self.move_right()
            self.B()

        elif self.read() == "+":
            self.write("0")
            self.move_right()
            self.halt()
        else:
            self.halting_error()

    def B(self):
        if self.verbose:
            print(f"B, {self.tape}, {self.position}")
        if self.read() == "1":
            self.move_right()
            self.B()
        elif self.read() == "+":
            self.move_right()
            self.C()
        else:
            self.halting_error()

    def C(self):
        if self.verbose:
            print(f"C, {self.tape}, {self.position}")
        if self.read() == "1":
            self.move_right()
            self.C()
        elif self.read() == "0":
            self.write("1")
            self.move_left()
            self.D()
        else:
            self.halting_error()

    def D(self):
        if self.verbose:
            print(f"D, {self.tape}, {self.position}")
        if self.read() == "1":
            self.move_left()
            self.D()
        elif self.read() == "+":
            self.move_left()
            self.E()
        else:
            self.halting_error()

    def E(self):
        if self.verbose:
            print(f"E, {self.tape}, {self.position}")
        if self.read() == "1":
            self.move_left()
            self.E()
        elif self.read() == "0":
            self.move_right()
            self.A()


if __name__ == "__main__":
    machine = AddingMachine("111+1111")
    machine.start()
