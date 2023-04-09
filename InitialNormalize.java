public class InitialNormalize {
    private String operandOne;
    private int exponentOne;
    private String operandTwo;
    private int exponentTwo;
    private boolean grs;
    private int digits;

    public InitialNormalize(String operandOne, int exponentOne, String operandTwo, int exponentTwo, boolean grs, int digits) {
        this.operandOne = operandOne;
        this.exponentOne = exponentOne;
        this.operandTwo = operandTwo;
        this.exponentTwo = exponentTwo;
        this.grs = grs;
        this.digits = digits;
    }

    public void shift() {
        if (exponentOne > exponentTwo) {
            char[] normalizedOperand = new char[operandTwo.length() + (exponentOne - exponentTwo)];
            int z = 0;

            for (int x = 0; x < operandTwo.length() + (exponentOne - exponentTwo); x++) {
                if (x != 1) { normalizedOperand[x] = '0'; } 
                else { normalizedOperand[x] = '.'; }
            }

            for (int y = (exponentOne - exponentTwo) + 1; y < operandTwo.length() + (exponentOne - exponentTwo); y++) {
                if (operandTwo.charAt(z) != '.') { normalizedOperand[y] = operandTwo.charAt(z); } 
                else { y--; }
                z++;
            }

            operandTwo = String.valueOf(normalizedOperand);
        } else if (exponentOne < exponentTwo) {
            char[] normalizedOperand = new char[operandOne.length() + (exponentTwo - exponentOne)];
            int z = 0;

            for (int x = 0; x < operandOne.length() + (exponentTwo - exponentOne); x++) {
                if (x != 1) { normalizedOperand[x] = '0'; } 
                else { normalizedOperand[x] = '.'; }
            }

            for (int y = (exponentTwo - exponentOne) + 1; y < operandOne.length() + (exponentTwo - exponentOne); y++) {
                if (operandOne.charAt(z) != '.') { normalizedOperand[y] = operandOne.charAt(z); } 
                else { y--; }
                z++;
            }

            operandOne = String.valueOf(normalizedOperand);
        }
    }

    public String getFirstOperand(){
        return operandOne;
    }

    public String getSecondOperand(){
        return operandTwo;
    }

    public static void main(String[] args) {
        InitialNormalize initialNormalize = new InitialNormalize("1.00111101", 5, "1.00111101", 3, false, 9);
        initialNormalize.shift();

        System.out.println(initialNormalize.getFirstOperand());
        System.out.println(initialNormalize.getSecondOperand());
    }
}
