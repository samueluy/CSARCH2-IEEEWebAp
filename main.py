import streamlit as st
from Operand import Operand
from Normalize import Normalize
from InitialNormalize import InitialNormalize
from Operation import Operation
from PostNormalize import PostNormalize

def main():
    
    st.write('<h1 style="font-size:32px; text-align:center">IEEE-754 binary-32 floating point operation</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    operand_one_input = col1.text_input('Enter first operand')
    operand_one_exponent = col2.number_input('Enter first exponent', value=0, step=1)

    col3, col4 = st.columns(2)
    operand_two_input = col3.text_input('Enter second operand')
    operand_two_exponent = col4.number_input('Enter second exponent', value=0, step=1)

    grs = st.checkbox("GRS?")
    digits = st.number_input("Number of digits supported:", value=0, step=1)

    first = Operand(operand_one_input, operand_one_exponent)
    second = Operand(operand_two_input, operand_two_exponent)
    # Check if values are empty
    if not operand_one_input or not operand_two_input:
        st.warning("Please enter both operands.")
    elif operand_one_input.strip() == "" or operand_two_input.strip() == "":
        st.warning("Please enter both operands.")
    elif operand_one_exponent is None or operand_two_exponent is None:
        st.warning("Please enter both exponents.")
    elif not (first.is_valid_input() and second.is_valid_input()):
        st.warning("There is an error with your input")
    else: # Success
        first_normalize = Normalize(first)
        second_normalize = Normalize(second)

        first_normalize.normalize()
        second_normalize.normalize()

        operand_one = first_normalize.binInput
        exponent_one = first_normalize.binExponent

        operand_two = second_normalize.binInput
        exponent_two = second_normalize.binExponent

        st.write('─' * 25)
        st.write("**Given:**")
        st.write(str(operand_one_input) + " 2x^" + str(operand_one_exponent))
        st.write(str(operand_two_input) + " 2x^" + str(operand_two_exponent))

        st.write('─' * 25)
        st.write("**Normalized**")
        st.write(str(operand_one) + " 2x^" + str(exponent_one))
        st.write(str(operand_two) + " 2x^" + str(exponent_two))

        initial_normalize = InitialNormalize(operand_one, exponent_one, operand_two, exponent_two, grs, digits)
        initial_normalize.performShift()
        initial_normalize.performRound()
        initial_normalize.performNegative()

        op1 = initial_normalize.getFirstOperand()
        op2 = initial_normalize.getSecondOperand()

        exp = initial_normalize.getExponent()

        st.write('─' * 25)
        st.write("**Initial Normalize:**")
        st.write("  " + str(op1) + " x2^" + str(exp))
        st.write(" " + str(op2) + " x2^" + str(exp))

        operation = Operation(initial_normalize.getFirstOperand(), initial_normalize.getSecondOperand(), grs, digits)
        operation.perform_addition()

        st.write('─' * 25)
        st.write("**Operation sum:**")
        st.write(" " + str(operation.get_sum()) + " x2^" + str(exp))

        post_normalize = PostNormalize(operation.sum, initial_normalize.exponent, digits)

        post_normalize.perform_shift()
        post_normalize.perform_round()

        st.write('─' * 25)
        st.write("**Post Operation:**")
        st.write("  " + str(post_normalize.get_sum()) + " x2^" + str(post_normalize.get_exponent()))

        text_output = '─' * 25 + '\n' + "Given:\n" + str(operand_one_input) + " 2x^" + str(operand_one_exponent) + '\n' + str(operand_two_input) + " 2x^" + str(operand_two_exponent) + '\n' + '─' * 25 + '\n' + "Normalized\n" + str(operand_one) + " 2x^" + str(exponent_one) + '\n' + str(operand_two) + " 2x^" + str(exponent_two) + '\n' + '─' * 25 + '\n' + \
            "Initial Normalize:\n" + str(op1) + " x2^" + str(exp) + '\n' + str(op2) + " x2^" + str(exp) + '\n' + '─' * 25 + '\n' + "Operation sum:\n" + str(
                operation.get_sum()) + " x2^" + str(exp) + '\n' + '─' * 25 + '\n' + "Post Operation:\n" + str(post_normalize.get_sum()) + " x2^" + str(post_normalize.get_exponent()) + '\n'

        st.download_button('Download output', text_output) 

if __name__ == "__main__":
    main()