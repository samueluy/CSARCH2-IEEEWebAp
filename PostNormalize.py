from Normalize import Normalize
from Operand import Operand
class PostNormalize:
    def __init__(self, sum_, exponent, digits):
        if sum_[0] == " ":
            adjusted_sum = [sum_[x + 1] for x in range(len(sum_) - 1)]
            self.sum = "".join(adjusted_sum)
        else:
            self.sum = sum_
        self.exponent = exponent
        self.digits = digits + 1

    def perform_shift(self):
        if len(self.sum) > 1 and self.sum[1] != ".":
            normalized_sum = [""] * len(self.sum)
            y = 0
            for x in range(len(self.sum)):
                if x == 1:
                    normalized_sum[x] = "."
                elif self.sum[y] == ".":
                    x -= 1
                    y += 1
                else:
                    normalized_sum[x] = self.sum[y]
                    y += 1
            self.sum = "".join(normalized_sum)
            self.exponent += 1

    def perform_round(self):
        rounded_sum = [""] * self.digits
        x = 0
        even = False
        while x < self.digits:
            rounded_sum[x] = self.sum[x]
            x += 1
        if len(self.sum) > x:
            if self.sum[x] == '1':
                for y in range(x + 1, len(self.sum), 1):
                    if(self.sum[y] == '1'):
                        rounded_sum = self.round_up(rounded_sum)
                        even = False
                        break
                    else:
                        even = True
                        
                if(self.sum[x - 1] == '1' and even):
                    rounded_sum = self.round_up(rounded_sum)
            
        self.sum = "".join(rounded_sum)

    def get_sum(self):
        return self.sum

    def get_exponent(self):
        return self.exponent

    def round_up(self, rounded_sum):
        overflow = True
        for x in range(self.digits - 1, 0, -1):
            if rounded_sum[x] == "1" and overflow:
                rounded_sum[x] = "0"
            elif rounded_sum[x] == "0" and overflow:
                rounded_sum[x] = "1"
                overflow = False
        return rounded_sum
    
    def check_normalize(self):
        operand = Operand(self.sum, self.exponent)
        if self.sum[0] != '-':
            if self.sum[0] != '1':
                output = Normalize(operand)
                output.normalize()
                output.setBinInput(append_filler(output.getBinInput(), self.digits))
                self.sum = output.getBinInput()
                self.exponent = output.getBinExponent()
                return output.getBinInput()
        else: # if negative
            if self.sum[1] != '1':
                output = Normalize(operand)
                output.normalize()
                output.setBinInput(append_filler(output.getBinInput(), self.digits))
                self.sum = output.getBinInput()
                self.digits = output.getBinExponent()
                return output.getBinInput()

        return self.sum
    
def append_filler(bin, digits):
    while len(bin) < digits:
        bin += '0'
    return bin