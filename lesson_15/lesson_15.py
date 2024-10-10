class Rhombus:
    def __init__(self, side_a, angel_a):
        self.side_a = side_a
        self.angel_a = angel_a
        self.angel_b = 180 - self.angel_a

    def __str__(self):
        return f"Side A: {self.side_a}, Angel A: {self.angel_a}, Angel B: {self.angel_b}"

    def __setattr__(self, name, value):
        if name == "side_a" and value <= 0:
            raise ValueError('Value of side a must be higher than 0')
        if name == "angel_a" and not (0 < value < 180):
            raise ValueError('Angle A must be between 0 and 180')
        super().__setattr__(name, value)
        if name == "angel_a":
            super().__setattr__("angel_b", 180 - value)
