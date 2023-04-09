public class InitialNormalize {
    private String operandOne;
    private int exponentOne;
    private String operandTwo;
    private int exponentTwo;
    private int exponent;
    private boolean grs;
    private int digits;

    public InitialNormalize(String operandOne, int exponentOne, String operandTwo, int exponentTwo, boolean grs, int digits) {
        this.operandOne  = operandOne;
        this.exponentOne = exponentOne;
        this.operandTwo  = operandTwo;
        this.exponentTwo = exponentTwo;
        this.exponent    = exponentOne;
        this.grs         = grs;
        this.digits      = digits + 1;
    }

    public void performShift() {
        if (this.exponentOne > this.exponentTwo) {
            char[] normalizedOperand = new char[this.operandTwo.length() + (this.exponentOne - this.exponentTwo)];
            int z = 0;

            for (int x = 0; x < this.operandTwo.length() + (this.exponentOne - this.exponentTwo); x++) {
                if (x != 1) { normalizedOperand[x] = '0'; } 
                else { normalizedOperand[x] = '.'; }
            }

            for (int y = (this.exponentOne - this.exponentTwo) + 1; y < this.operandTwo.length() + (this.exponentOne - this.exponentTwo); y++) {
                if (this.operandTwo.charAt(z) != '.') { normalizedOperand[y] = this.operandTwo.charAt(z); }
                else { y--; }
                z++;
            }

            this.exponent = this.exponentOne;
            this.operandTwo = String.valueOf(normalizedOperand);
        } else if (this.exponentOne < this.exponentTwo) {
            char[] normalizedOperand = new char[this.operandOne.length() + (this.exponentTwo - this.exponentOne)];
            int z = 0;

            for (int x = 0; x < this.operandOne.length() + (this.exponentTwo - this.exponentOne); x++) {
                if (x != 1) { normalizedOperand[x] = '0'; } 
                else { normalizedOperand[x] = '.'; }
            }

            for (int y = (this.exponentTwo - this.exponentOne) + 1; y < this.operandOne.length() + (this.exponentTwo - this.exponentOne); y++) {
                if (this.operandOne.charAt(z) != '.') { normalizedOperand[y] = this.operandOne.charAt(z); } 
                else { y--; }
                z++;
            }

            this.exponent = this.exponentTwo;
            this.operandOne = String.valueOf(normalizedOperand);
        } else { this.exponent = this.exponentTwo; }
    }

    public void performRound() {
        if (!this.grs) {
            char[] roundedOperandOne = new char[this.digits];
            char[] roundedOperandTwo = new char[this.digits];
            int x = 0;

            while (x < this.digits) {
                roundedOperandOne[x] = this.operandOne.charAt(x);
                roundedOperandTwo[x] = this.operandTwo.charAt(x);
                x++;
            }

            if (this.operandOne.length() > x) { if (this.operandOne.charAt(x) == '1') { roundedOperandOne = roundUp(roundedOperandOne); } }

            if (this.operandOne.length() > x) { if (this.operandTwo.charAt(x) == '1') { roundedOperandTwo = roundUp(roundedOperandTwo); } }

            this.operandOne = String.valueOf(roundedOperandOne);
            this.operandTwo = String.valueOf(roundedOperandTwo);
        } else {
            char[] roundedOperandOne = new char[(this.digits + 3)];
            char[] roundedOperandTwo = new char[(this.digits + 3)];
            int x = 0;

            while(x < this.digits + 2) {
                roundedOperandOne[x] = this.operandOne.charAt(x);
                roundedOperandTwo[x] = this.operandTwo.charAt(x);
                x++;
            }
            
            roundedOperandOne[x] = nonZero(this.operandOne);
            roundedOperandTwo[x] = nonZero(this.operandTwo);

            this.operandOne = String.valueOf(roundedOperandOne);
            this.operandTwo = String.valueOf(roundedOperandTwo);
        }
    }

    public String getFirstOperand() { return this.operandOne; }

    public String getSecondOperand() { return this.operandTwo; }

    public int getExponent() { return this.exponent; }

    private char[] roundUp(char[] roundedOperand) {
        boolean overflow = true;

        for (int x = this.digits - 1; x > 0 && overflow; x--) {
            if (roundedOperand[x] == '1' && overflow) { roundedOperand[x] = '0'; } 
            else if (roundedOperand[x] == '0' && overflow){
                roundedOperand[x] = '1';
                overflow = false;
            }
        }

        return roundedOperand;
    }

    private char nonZero(String operand) {
        boolean nonZero = true;

        for (int x = (this.digits + 2); x < operand.length() && nonZero; x++) { if (operand.charAt(x) == '1') { nonZero = false; } }

        if (nonZero == false) { return '1'; }

        return '0';
    }
}
