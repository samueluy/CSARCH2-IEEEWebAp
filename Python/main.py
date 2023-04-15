import streamlit as st
from Operand import Operand
from Normalize import Normalize
from InitialNormalize import InitialNormalize
from Operation import Operation
from PostNormalize import PostNormalize

def main():
    st.title("Floating Point Multiplication")

    operand_one_input = st.text_input("Enter first operand:", "110111.11011111")
    operand_one_base = st.slider("Select base for first operand:", 2, 16, 10)

    operand_two_input = st.text_input("Enter second operand:", "111111.0100101")
    operand_two_base = st.slider("Select base for second operand:", 2, 16, 8)

    grs = False
    digits = 4

    first = Operand(operand_one_input, operand_one_base)
    second = Operand(operand_two_input, operand_two_base)

    first_normalize = Normalize(first)
    second_normalize = Normalize(second)

    first_normalize.normalize()
    second_normalize.normalize()

    operand_one = first_normalize.binInput
    exponent_one = first_normalize.binExponent

    operand_two = second_normalize.binInput
    exponent_two = second_normalize.binExponent

    initial_normalize = InitialNormalize(operand_one, exponent_one, operand_two, exponent_two, grs, digits)

    initial_normalize.performShift()
    initial_normalize.performRound()
    initial_normalize.performRound()

    op1 = initial_normalize.getFirstOperand()
    op2 = initial_normalize.getSecondOperand()

    exp = initial_normalize.getExponent()

    st.write("  " + str(op1) + " x2^" + str(exp))
    st.write(" " + str(op2) + " x2^" + str(exp))

    operation = Operation(initial_normalize.getFirstOperand(), initial_normalize.getFirstOperand(), grs, digits)
    operation.perform_addition()

    st.write("-------------")
    st.write(" " + str(operation.get_sum()) + " x2^" + str(exp))

    post_normalize = PostNormalize(operation.sum, initial_normalize.exponent, digits)

    post_normalize.perform_shift()
    post_normalize.perform_round()

    st.write("-------------")
    st.write("  " + str(post_normalize.get_sum()) + " x2^" + str(post_normalize.get_exponent()))

if __name__ == "__main__":
    main()
