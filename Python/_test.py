from Operand import Operand
from Normalize import Normalize
from InitialNormalize import InitialNormalize
from Operation import Operation
from PostNormalize import PostNormalize

first = Operand("110111.11011111", 10)
second = Operand("111111.0100101", 8)
first_normalize = Normalize(first)
second_normalize = Normalize(second)
first_normalize.normalize()
second_normalize.normalize()
operand_one = first_normalize.binInput
exponent_one = first_normalize.binExponent
operand_two = second_normalize.binInput
exponent_two = second_normalize.binExponent
grs = False
digits = 4

# Use Samuel Uy's Normalization here if operands are crazy like 1000.1111 and not in 1.f 

initial_normalize = InitialNormalize(operand_one, exponent_one, operand_two, exponent_two, grs, digits)
initial_normalize.performShift()
initial_normalize.performRound()
initial_normalize.performRound()

op1 = initial_normalize.getFirstOperand()
op2 = initial_normalize.getSecondOperand()

exp = initial_normalize.getExponent()

print("  " + str(op1) + " x2^" + str(exp))
print(" " + str(op2) + " x2^" + str(exp))


operation = Operation(initial_normalize.getFirstOperand(), initial_normalize.getFirstOperand(), grs, digits)
operation.perform_addition()
print("-------------")
print(" " + str(operation.get_sum()) + " x2^" + str(exp))

post_normalize = PostNormalize(operation.sum, initial_normalize.exponent, digits)
post_normalize.perform_shift()
post_normalize.perform_round()
print("-------------")
print("  " + str(post_normalize.get_sum()) + " x2^" + str(post_normalize.get_exponent()))


