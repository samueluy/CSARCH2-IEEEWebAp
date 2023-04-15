class Normalize:
    def __init__(self, operand):
        self.binInput = operand.binary
        self.binExponent = operand.exponent

    def normalize(self):
        binary = self.getBinInput()
        exponent = self.getBinExponent()

        newBinary = list(binary)
        radixLoc = 0
        oneLoc = 0

        # look for the decimal point
        for i, char in enumerate(binary):
            if char == '.':
                radixLoc = i
                break

        # look for first 1
        for i, char in enumerate(binary):
            if char == '1':
                oneLoc = i
                break

        if binary[0] == '-':  # if value is negative
            del newBinary[radixLoc]
            if oneLoc > 0:
                if radixLoc < oneLoc:
                    del newBinary[1:oneLoc - 1]  # trim zeroes at the start
                else:
                    del newBinary[1:oneLoc]  # trim zeroes at the start
            newBinary.insert(2, '.')  # add radix point after first 1

            # modify exponent value
            if radixLoc < oneLoc:
                exponent = exponent - (oneLoc - radixLoc)
            elif oneLoc < radixLoc:
                exponent = exponent + ((radixLoc - 1) - oneLoc)
        else:
            # generate new string
            del newBinary[radixLoc]  # delete radix point
            if oneLoc > 0:
                if radixLoc < oneLoc:
                    del newBinary[:oneLoc - 1]  # trim zeroes at the start
                else:
                    del newBinary[:oneLoc]  # trim zeroes at the start

            newBinary.insert(1, '.')  # add radix point after first 1

            # modify exponent value
            if radixLoc < oneLoc:
                exponent = exponent - (oneLoc - radixLoc)
            elif oneLoc < radixLoc:
                exponent = exponent + ((radixLoc - 1) - oneLoc)

        self.setBinInput(''.join(newBinary))
        self.setBinExponent(exponent)

    def getBinInput(self):
        return self.binInput

    def getBinExponent(self):
        return self.binExponent

    def setBinInput(self, binInput):
        self.binInput = binInput

    def setBinExponent(self, binExponent):
        self.binExponent = binExponent
