# IEEE-754 Binary-32 Floating Point Operation

This code performs IEEE-754 binary-32 floating point operations. It allows users to input two operands, specify their exponents, and perform addition on them. The code normalizes the operands, performs the addition operation, and provides the result in normalized form.

## Functionality

1. User Input: The code prompts the user to enter two operands and their corresponding exponents.
2. Normalization: The operands are normalized using the IEEE-754 standard.
3. Initial Normalize: The operands are further processed by performing shift, rounding, and handling negative numbers.
4. Addition: The addition operation is performed on the normalized operands.
5. Post Operation: The result of the addition is post-normalized to ensure it adheres to the IEEE-754 format.
6. Output: The code displays the input operands, their normalized forms, the initial normalized operands, the sum of the operands after addition, and the post-normalized result.
7. Download: Users can download the output as a text file.

## Usage

1. Enter the first operand and its exponent in the designated input fields.
2. Enter the second operand and its exponent in the designated input fields.
3. Check the "GRS?" checkbox if desired.
4. Specify the number of digits supported.
5. Click the "Download output" button to save the output as a text file.

Please ensure that all inputs are provided correctly to obtain accurate results.

Note: The code uses the Streamlit library for the user interface and relies on custom classes such as `Operand`, `Normalize`, `InitialNormalize`, `Operation`, and `PostNormalize` to perform the necessary calculations and transformations.
