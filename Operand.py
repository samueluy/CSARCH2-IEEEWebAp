class Operand:
    def __init__(self, binary, exponent):
        self.binary = binary
        self.exponent = exponent

    def is_valid_input(self):
        if self.binary == "":
            return False
        if not all(bit in '01.-' for bit in self.binary):
            return False
        if not isinstance(self.exponent, int):
            return False
        if '.' in self.binary:
            decimal_points = self.binary.count('.')
            if decimal_points != 1:
                return False
        if '-' in self.binary:
            minus_sign = self.binary.count('-')
            if minus_sign != 1:
                return False
        return True
