public class _test {
    public static void main(String[] args){
        Operand first = new Operand("000.11011111011111", 10);
        Operand second = new Operand("000.1111110100101", 8);


        // Print Given
        System.out.println("Given:");
        System.out.println("  " + first.binary + " x2^" + first.exponent);
        System.out.println("  " + second.binary + " x2^" + second.exponent);
        System.out.println("-------------");


        // Normalize
        Normalize firstNormalize = new Normalize(first);
        Normalize secondNormalize = new Normalize(second);
        firstNormalize.normalize();
        secondNormalize.normalize();
        String operandOne = firstNormalize.getBinInput();    int exponentOne = firstNormalize.getBinExponent();
        String operandTwo = secondNormalize.getBinInput();   int exponentTwo = secondNormalize.getBinExponent();
        boolean grs = true;            int digits = 7; // number of bits

        /* Use @Samuel Uy's Normalization here if operands are crazy like 1000.1111 and not in 1.f */
        InitialNormalize initialNormalize = new InitialNormalize(operandOne, exponentOne, operandTwo, exponentTwo, grs, digits);
        initialNormalize.performShift();
        initialNormalize.performRound();
        initialNormalize.performNegative();

        System.out.println("Initial normalization");
        System.out.println("  " + initialNormalize.getFirstOperand() + " x2^" + initialNormalize.getExponent());
        System.out.println("  " + initialNormalize.getSecondOperand() + " x2^" + initialNormalize.getExponent());

        Operation operation = new Operation(initialNormalize.getFirstOperand(), initialNormalize.getSecondOperand(), grs, digits);
        operation.performAddition();
        System.out.println("-------------");
        System.out.println("Operation sum:");
        System.out.println(" " + operation.getSum() + " x2^" + initialNormalize.getExponent());

        PostNormalize postNormalize = new PostNormalize(operation.getSum(), initialNormalize.getExponent(), digits);
        postNormalize.performShift();
        postNormalize.performRound();
        System.out.println("-------------");
        System.out.println("Post operation normalization (final answer)");

        System.out.println("  " + postNormalize.getSum() + " x2^" + postNormalize.getExponent());

        /* Use @Samuel Uy's Normalization here if sum is 0.0001 and not in 10.f */
    }
}
