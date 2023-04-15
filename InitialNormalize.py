class InitialNormalize(object) :
    negativeOne = False
    operandOne = None
    exponentOne = 0
    negativeTwo = False
    operandTwo = None
    exponentTwo = 0
    exponent = 0
    grs = False
    digits = 0
    def __init__(self, operandOne,  exponentOne,  operandTwo,  exponentTwo,  grs,  digits) :
        if (operandOne[0] == '-') :
            operandHolder = [' '] * (len(operandOne))
            x = 0
            while (x < len(operandOne) - 1) :
                operandHolder[x] = operandOne[x + 1]
                x += 1
            self.operandOne = "".join(operandHolder)
            self.negativeOne = True
        else :
            self.operandOne = operandOne
            self.negativeOne = False
        self.exponentOne = exponentOne
        if (operandTwo[0] == '-') :
            operandHolder = [' '] * (len(operandTwo))
            x = 0
            while (x < len(operandTwo) - 1) :
                operandHolder[x] = operandTwo[x + 1]
                x += 1
            self.operandTwo = "".join(operandHolder)
            self.negativeTwo = True
        else :
            self.operandTwo = operandTwo
            self.negativeTwo = False
        self.exponentTwo = exponentTwo
        self.exponent = exponentOne
        self.grs = grs
        self.digits = digits + 1
    def performShift(self) :
        if (self.exponentOne > self.exponentTwo) :
            normalizedOperand = [' '] * (len(self.operandTwo) + (self.exponentOne - self.exponentTwo))
            z = 0
            x = 0
            while (x < len(self.operandTwo) + (self.exponentOne - self.exponentTwo)) :
                if (x != 1) :
                    normalizedOperand[x] = '0'
                else :
                    normalizedOperand[x] = '.'
                x += 1
            y = (self.exponentOne - self.exponentTwo) + 1
            while (y < len(self.operandTwo) + (self.exponentOne - self.exponentTwo)) :
                if (self.operandTwo[z] != '.') :
                    normalizedOperand[y] = self.operandTwo[z]
                else :
                    y -= 1
                z += 1
                y += 1
            self.exponent = self.exponentOne
            self.operandTwo = "".join(normalizedOperand)
        elif(self.exponentOne < self.exponentTwo) :
            normalizedOperand = [' '] * (len(self.operandOne) + (self.exponentTwo - self.exponentOne))
            z = 0
            x = 0
            while (x < len(self.operandOne) + (self.exponentTwo - self.exponentOne)) :
                if (x != 1) :
                    normalizedOperand[x] = '0'
                else :
                    normalizedOperand[x] = '.'
                x += 1
            y = (self.exponentTwo - self.exponentOne) + 1
            while (y < len(self.operandOne) + (self.exponentTwo - self.exponentOne)) :
                if (self.operandOne[z] != '.') :
                    normalizedOperand[y] = self.operandOne[z]
                else :
                    y -= 1
                z += 1
                y += 1
            self.exponent = self.exponentTwo
            self.operandOne = "".join(normalizedOperand)
        else :
            self.exponent = self.exponentTwo
    def performRound(self) :
        if (not self.grs) :
            roundedOperandOne = [' '] * (self.digits)
            roundedOperandTwo = [' '] * (self.digits)
            x = 0
            evenOne = False
            evenTwo = False
            while (x < self.digits) :
                try:
                    roundedOperandOne[x] = self.operandOne[x]
                    roundedOperandTwo[x] = self.operandTwo[x]
                    x += 1
                except: # filler digits
                    roundedOperandOne+='0'
                    roundedOperandTwo+='0'
                    x += 1

            if (len(self.operandOne) > x) :
                if (self.operandOne[x] == '1') :
                    for y in range(x + 1 , len(self.operandOne), 1):
                        if (self.operandOne[y] == '1') :
                            roundedOperandOne = self.roundUp(roundedOperandOne)
                            evenOne = False
                            break
                        else:
                            evenOne = True
                    
                    if (self.operandOne[x - 1] == '1' and evenOne) :
                        roundedOperandOne = self.roundUp(roundedOperandOne)
                        
            if (len(self.operandTwo) > x) :
                if (self.operandTwo[x] == '1') :
                    for y in range(x + 1, len(self.operandTwo), 1):
                        if (self.operandTwo[y] == '1') :
                            roundedOperandTwo = self.roundUp(roundedOperandTwo)
                            evenTwo = False
                            break
                        else:
                            evenTwo = True
                            
                    if (self.operandTwo[x - 1] == '1' and evenTwo) :
                        roundedOperandTwo = self.roundUp(roundedOperandTwo)
                    
            self.operandOne = "".join(roundedOperandOne)
            self.operandTwo = "".join(roundedOperandTwo)
        else :
            roundedOperandOne = [' '] * ((self.digits + 3))
            roundedOperandTwo = [' '] * ((self.digits + 3))
            x = 0
            while (x < self.digits + 2) :
                try:
                    roundedOperandOne[x] = self.operandOne[x]
                    roundedOperandTwo[x] = self.operandTwo[x]
                    x += 1
                except: # filler digits
                    roundedOperandOne+='0'
                    roundedOperandTwo+='0'
                    x += 1
            roundedOperandOne[x] = self.nonZero(self.operandOne)
            roundedOperandTwo[x] = self.nonZero(self.operandTwo)
            self.operandOne = "".join(roundedOperandOne)
            self.operandTwo = "".join(roundedOperandTwo)
    def performNegative(self) :
        if (self.negativeOne) :
            operandHolder = [' '] * (len(self.operandOne) + 1)
            operandHolder[0] = '-'
            x = 1
            while (x < len(self.operandOne) + 1) :
                operandHolder[x] = self.operandOne[x - 1]
                x += 1
            self.operandOne = "".join(operandHolder)
            self.negativeOne = False
        if (self.negativeTwo) :
            operandHolder = [' '] * (len(self.operandTwo) + 1)
            operandHolder[0] = '-'
            x = 1
            while (x < len(self.operandTwo) + 1) :
                operandHolder[x] = self.operandTwo[x - 1]
                x += 1
            self.operandTwo = "".join(operandHolder)
            self.negativeOne = False
    def  getFirstOperand(self) :
        return self.operandOne
    def  getSecondOperand(self) :
        return self.operandTwo
    def  getExponent(self) :
        return self.exponent
    def  roundUp(self, roundedOperand) :
        overflow = True
        x = self.digits - 1
        while (x > 0 and overflow) :
            if (roundedOperand[x] == '1' and overflow) :
                roundedOperand[x] = '0'
            elif(roundedOperand[x] == '0' and overflow) :
                roundedOperand[x] = '1'
                overflow = False
            x -= 1
        return roundedOperand
    def  nonZero(self, operand) :
        nonZero = True
        x = (self.digits + 2)
        while (x < len(operand) and nonZero) :
            if (operand[x] == '1') :
                nonZero = False
            x += 1
        if (nonZero == False) :
            return '1'
        return '0'