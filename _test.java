public class _test {
    public static void main(String[] args){
        String operandOne = "1.0111110010011";
        int exponentOne = 5;
        String operandTwo = "1.00111111100011";
        int exponentTwo = 3;
        boolean grs = true;
        int digits = 9;

        InitialNormalize initialNormalize = new InitialNormalize(operandOne, exponentOne, operandTwo, exponentTwo, grs, digits);
        initialNormalize.performShift();
        initialNormalize.performRound();

        System.out.println(" " + initialNormalize.getFirstOperand() + " " + initialNormalize.getExponent());
        System.out.println(" " + initialNormalize.getSecondOperand() + " " + initialNormalize.getExponent());

        Operation operation = new Operation(initialNormalize.getFirstOperand(), initialNormalize.getSecondOperand(), grs, digits);
        operation.performAddition();
        System.out.println(operation.getSum() + " " + initialNormalize.getExponent());

        PostNormalize postNormalize = new PostNormalize(operation.getSum(), initialNormalize.getExponent(), digits);
        postNormalize.performShift();
        postNormalize.performRound();

        System.out.println(" " + postNormalize.getSum() + " " + postNormalize.getExponent());
    }
}
