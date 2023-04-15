class InitialNormalize:
    def __init__(self, operandOne, exponentOne, operandTwo, exponentTwo, grs, digits):
        self.negativeOne = False
        self.negativeTwo = False
        if operandOne[0] == '-':
            operandHolder = [0] * len(operandOne)
            for x in range(len(operandOne) - 1):
                operandHolder[x] = operandOne[x + 1]
            self.operandOne = ''.join(operandHolder)
            self.negativeOne = True
        else:
            self.operandOne = operandOne
        self.exponentOne = exponentOne
        if operandTwo[0] == '-':
            operandHolder = [0] * len(operandTwo)
            for x in range(len(operandTwo) - 1):
                operandHolder[x] = operandTwo[x + 1]
            self.operandTwo = ''.join(operandHolder)
            self.negativeTwo = True
        else:
            self.operandTwo = operandTwo

        self.exponentTwo = exponentTwo
        self.exponent = exponentOne
        self.grs = grs
        self.digits = digits + 1

    def performShift(self):
        if self.exponentOne > self.exponentTwo:
            normalizedOperand = ['0'] * (len(self.operandTwo) + (self.exponentOne - self.exponentTwo))
            z = 0
            for x in range(len(self.operandTwo) + (self.exponentOne - self.exponentTwo)):
                if x != 1:
                    normalizedOperand[x] = '0'
                else:
                    normalizedOperand[x] = '.'
            for y in range((self.exponentOne - self.exponentTwo) + 1, len(self.operandTwo) + (self.exponentOne - self.exponentTwo)):
                if self.operandTwo[z] != '.':
                    normalizedOperand[y] = self.operandTwo[z]
                else:
                    y -= 1
                z += 1
            self.exponent = self.exponentOne
            self.operandTwo = ''.join(normalizedOperand)
        elif self.exponentOne < self.exponentTwo:
            normalizedOperand = ['0'] * (len(self.operandOne) + (self.exponentTwo - self.exponentOne))
            z = 0
            for x in range(len(self.operandOne) + (self.exponentTwo - self.exponentOne)):
                if x != 1:
                    normalizedOperand[x] = '0'
                else:
                    normalizedOperand[x] = '.'
            for y in range((self.exponentTwo - self.exponentOne) + 1, len(self.operandOne) + (self.exponentTwo - self.exponentOne)):
                if self.operandOne[z] != '.':
                    normalizedOperand[y] = self.operandOne[z]
                else:
                    y -= 1
                z += 1
            self.exponent = self.exponentTwo
            self.operandOne = ''.join(normalizedOperand)
        else:
            self.exponent = self.exponentTwo

    def performRound(self):
        if not self.grs:
            roundedOperandOne = [0] * self.digits
            roundedOperandTwo = [0] * self.digits
            x = 0

            while x < self.digits:
                roundedOperandOne[x] = self.operandOne[x]
                roundedOperandTwo[x] = self.operandTwo[x]
                x += 1

            if len(self.operandOne) > x:
                if self.operandOne[x] == '1':
                    roundedOperandOne = self.roundUp(roundedOperandOne)

            if len(self.operandTwo) > x:
                if self.operandTwo[x] == '1':
                    roundedOperandTwo = self.roundUp(roundedOperandTwo)

            self.operandOne = ''.join(str(x) for x in roundedOperandOne)
            self.operandTwo = ''.join(str(x) for x in roundedOperandTwo)
        else:
            roundedOperandOne = [0] * (self.digits + 3)
            roundedOperandTwo = [0] * (self.digits + 3)
            x = 0

            while x < self.digits + 2:
                roundedOperandOne[x] = self.operandOne[x]
                roundedOperandTwo[x] = self.operandTwo[x]
                x += 1
            
            roundedOperandOne[x] = self.nonZero(self.operandOne)
            roundedOperandTwo[x] = self.nonZero(self.operandTwo)

            self.operandOne = ''.join(str(x) for x in roundedOperandOne)
            self.operandTwo = ''.join(str(x) for x in roundedOperandTwo)


    def performNegative(self):
        if self.negativeOne:
            operandHolder = ['-'] + list(self.operandOne)
            self.operandOne = ''.join(str(x) for x in operandHolder)
            self.negativeOne = False
            
        if self.negativeTwo:
            operandHolder = ['-'] + list(self.operandTwo)
            self.operandTwo = ''.join(str(x) for x in operandHolder)
            self.negativeTwo = False


    def getFirstOperand(self):
        return self.operandOne


    def getSecondOperand(self):
        return self.operandTwo


    def getExponent(self):
        return self.exponent


    def roundUp(self, roundedOperand):
        overflow = True

        for x in range(self.digits - 1, 0, -1):
            if roundedOperand[x] == 1 and overflow:
                roundedOperand[x] = 0
            elif roundedOperand[x] == 0 and overflow:
                roundedOperand[x] = 1
                overflow = False

        return roundedOperand


    def nonZero(self, operand):
        nonZero = True

        for x in range(self.digits + 2, len(operand)):
            if operand[x] == '1':
                nonZero = False
                break

        if nonZero == False:
            return '1'

        return '0'