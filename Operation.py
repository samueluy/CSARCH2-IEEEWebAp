class Operation(object) :
    firstOperand = None
    secondOperand = None
    digits = 0
    sum = None
    overflow = False
    signed = False
    def __init__(self, firstOperand,  secondOperand,  grs,  digits) :
        self.firstOperand = firstOperand
        self.secondOperand = secondOperand
        if (not grs) :
            self.digits = digits + 1
        else :
            self.digits = (digits + 3) + 1
        self.sum = [' '] * (self.digits + 1)
        self.overflow = False
        self.signed = False
        x = 0
        while (x < self.digits + 1) :
            self.sum[x] = ' '
            x += 1
    def perform_addition(self) :
        if (self.firstOperand[0] == '-') :
            self.firstOperand = "".join(self.perform_complement(self.firstOperand))
            self.signed = True
        elif(self.secondOperand[0] == '-') :
            self.secondOperand = "".join(self.perform_complement(self.secondOperand))
            self.signed = True
        x = self.digits - 1
        while (x >= 0) :
            if (self.firstOperand[x] == '1' and self.secondOperand[x] == '1' and self.overflow) :
                self.sum[x + 1] = '1'
                self.overflow = True
            elif(self.firstOperand[x] == '1' and self.secondOperand[x] == '1' and not self.overflow) :
                self.sum[x + 1] = '0'
                self.overflow = True
            elif(self.firstOperand[x] == '1' and self.secondOperand[x] == '0' and self.overflow or self.firstOperand[x] == '0' and self.secondOperand[x] == '1' and self.overflow) :
                self.sum[x + 1] = '0'
                self.overflow = True
            elif(self.firstOperand[x] == '1' and self.secondOperand[x] == '0' and not self.overflow or self.firstOperand[x] == '0' and self.secondOperand[x] == '1' and not self.overflow) :
                self.sum[x + 1] = '1'
                self.overflow = False
            elif(self.firstOperand[x] == '0' and self.secondOperand[x] == '0' and self.overflow) :
                self.sum[x + 1] = '1'
                self.overflow = False
            elif(self.firstOperand[x] == '0' and self.secondOperand[x] == '0' and not self.overflow) :
                self.sum[x + 1] = '0'
                self.overflow = False
            else :
                self.sum[x + 1] = '.'
            x -= 1
        if (self.overflow and not self.signed) :
            self.sum[0] = '1'
    def  get_sum(self) :
        return "".join(self.sum)
    def  perform_complement(self, negative) :
        positive = [' '] * (self.digits)
        firstOne = False
        x = 0
        while (x < self.digits) :
            positive[x] = ' '
            x += 1
        x = self.digits - 1
        while (x >= 0) :
            if (negative[x + 1] == '1' and not firstOne) :
                positive[x] = '1'
                firstOne = True
            elif(negative[x + 1] == '0' and not firstOne) :
                positive[x] = '0'
            elif(negative[x + 1] == '1' and firstOne) :
                positive[x] = '0'
            elif(negative[x + 1] == '0' and firstOne) :
                positive[x] = '1'
            else :
                positive[x] = '.'
            x -= 1
        return positive