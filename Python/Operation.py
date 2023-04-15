class Operation:
    def __init__(self, first_operand, second_operand, grs, digits):
        self.first_operand = first_operand
        self.second_operand = second_operand

        if not grs:
            self.digits = digits + 1
        else:
            self.digits = (digits + 3) + 1

        self.sum = [' '] * (self.digits + 1)
        self.overflow = False
        self.signed = False

    def perform_addition(self):
        if self.first_operand[0] == '-':
            self.first_operand = str(self.perform_complement(self.first_operand))
            self.signed = True
        elif self.second_operand[0] == '-':
            self.second_operand = str(self.perform_complement(self.second_operand))
            self.signed = True

        for x in range(self.digits - 1, -1, -1):
            if (self.first_operand[x] == '1' and self.second_operand[x] == '1' and self.overflow):
                self.sum[x + 1] = '1'
                self.overflow = True
            elif (self.first_operand[x] == '1' and self.second_operand[x] == '1' and not self.overflow):
                self.sum[x + 1] = '0'
                self.overflow = True
            elif ((self.first_operand[x] == '1' and self.second_operand[x] == '0' and self.overflow) or
                  (self.first_operand[x] == '0' and self.second_operand[x] == '1' and self.overflow)):
                self.sum[x + 1] = '0'
                self.overflow = True
            elif ((self.first_operand[x] == '1' and self.second_operand[x] == '0' and not self.overflow) or
                  (self.first_operand[x] == '0' and self.second_operand[x] == '1' and not self.overflow)):
                self.sum[x + 1] = '1'
                self.overflow = False
            elif (self.first_operand[x] == '0' and self.second_operand[x] == '0' and self.overflow):
                self.sum[x + 1] = '1'
                self.overflow = False
            elif (self.first_operand[x] == '0' and self.second_operand[x] == '0' and not self.overflow):
                self.sum[x + 1] = '0'
                self.overflow = False
            else:
                self.sum[x + 1] = '.'

        if self.overflow and not self.signed:
            self.sum[0] = '1'

    def get_sum(self):
        return ''.join(self.sum)

    def perform_complement(self, negative):
        positive = [' '] * self.digits
        first_one = False

        for x in range(self.digits):
            positive[x] = ' '

        for x in range(self.digits - 1, -1, -1):
            if negative[x + 1] == '1' and not first_one:
                positive[x] = '1'
                first_one = True
            elif negative[x + 1] == '0' and not first_one:
                positive[x] = '0'
            elif negative[x + 1] == '1' and first_one:
                positive[x] = '0'
            elif negative[x + 1] == '0' and first_one:
                positive[x] = '1'
            else:
                positive[x] = '.'

        return positive