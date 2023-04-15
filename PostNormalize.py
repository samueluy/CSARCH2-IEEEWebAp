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
        if self.sum[1] != ".":
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
        while x < self.digits:
            rounded_sum[x] = self.sum[x]
            x += 1
        if len(self.sum) > x:
            if self.sum[x] == "1":
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