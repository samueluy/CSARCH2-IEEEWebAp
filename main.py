import streamlit as st
from Operand import Operand
from Normalize import Normalize
from InitialNormalize import InitialNormalize
from Operation import Operation
from PostNormalize import PostNormalize

def main():
    try:
        st.title("Floating Point Multiplication")

        operand_one_input = st.text_input("Enter first operand:", "")
        operand_one_exponent = st.text_input("Enter first exponent", "")

        operand_two_input = st.text_input("Enter second operand:", "")
        operand_two_exponent = st.text_input("Enter second exponent:", "")

        grs = st.checkbox("GRS?")
        digits = st.text_input("Supports how many digits:", "")

        first = Operand(operand_one_input, operand_one_exponent)
        second = Operand(operand_two_input, operand_two_exponent)

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
        initial_normalize.performNegative()

        op1 = initial_normalize.getFirstOperand()
        op2 = initial_normalize.getSecondOperand()

        exp = initial_normalize.getExponent()

        st.write("  " + str(op1) + " x2^" + str(exp))
        st.write(" " + str(op2) + " x2^" + str(exp))

        operation = Operation(initial_normalize.getFirstOperand(), initial_normalize.getSecondOperand(), grs, digits)
        operation.perform_addition()

        st.write('─' * 25)
        st.write(" " + str(operation.get_sum()) + " x2^" + str(exp))

        post_normalize = PostNormalize(operation.sum, initial_normalize.exponent, digits)

        post_normalize.perform_shift()
        post_normalize.perform_round()

        st.write('─' * 25)
        st.write("  " + str(post_normalize.get_sum()) + " x2^" + str(post_normalize.get_exponent()))
    except:
        st.write("Error has occured! Please try again.")

if __name__ == "__main__":
    main()