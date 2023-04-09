public class Operation {
    private String firstOperand;
    private String secondOperand;
    private int digits;
    private char[] sum;
    private boolean overflow;
    private boolean signed;

    public Operation(StringBuilder firstOperand, StringBuilder secondOperand, int digits) {
        this.firstOperand   = firstOperand.toString();
        this.secondOperand  = secondOperand.toString();
        this.digits         = digits + 1;                   // binary digits + dot
        this.sum            = new char[this.digits + 1];    // (binary digits + dot) + overflow
        this.overflow       = false;
        this.signed         = false;

        for (int x = 0; x < this.digits + 1; x++) { sum[x] = ' '; }
    }

    public Operation(String firstOperand, String secondOperand, int digits) {
        this.firstOperand   = firstOperand;
        this.secondOperand  = secondOperand;
        this.digits         = digits + 1;                   // binary digits + dot
        this.sum            = new char[this.digits + 1];    // (binary digits + dot) + overflow
        this.overflow       = false;
        this.signed         = false;

        for (int x = 0; x < this.digits + 1; x++) { sum[x] = ' '; }
    }

    public char[] performComplement(String negative) {
        char[] positive = new char[this.digits];
        boolean firstOne = false;

        for (int x = 0; x < this.digits; x++) { positive[x] = ' '; }

        for (int x = this.digits - 1; x >= 0; x--) {
            if (negative.charAt(x + 1) == '1' && !firstOne) {
                positive[x] = '1';
                firstOne = true;
            } 
            else if (negative.charAt(x + 1) == '0' && !firstOne) { positive[x] = '0'; } 
            else if (negative.charAt(x + 1) == '1' && firstOne) { positive[x] = '0'; } 
            else if (negative.charAt(x + 1) == '0' && firstOne) { positive[x] = '1'; } 
            else { positive[x] = '.'; }
        }

        return positive;
    }

    public void performAddition() {
        if (this.firstOperand.charAt(0) == '-') {
            firstOperand = String.valueOf(performComplement(firstOperand));
            this.signed = true;
        } else if (this.secondOperand.charAt(0) == '-') {
            secondOperand = String.valueOf(performComplement(secondOperand));
            this.signed = true;
        }

        for (int x = this.digits - 1; x >= 0; x--) {
            if (this.firstOperand.charAt(x) == '1' && this.secondOperand.charAt(x) == '1' && this.overflow) {
                this.sum[x + 1] = '1';
                this.overflow   = true;
            } else if (this.firstOperand.charAt(x) == '1' && this.secondOperand.charAt(x) == '1' && !this.overflow) {
                this.sum[x + 1] = '0';
                this.overflow   = true;
            } else if (this.firstOperand.charAt(x) == '1' && this.secondOperand.charAt(x) == '0' && this.overflow
                    || this.firstOperand.charAt(x) == '0' && this.secondOperand.charAt(x) == '1' && this.overflow) {
                this.sum[x + 1] = '0';
                this.overflow   = true;
            } else if (this.firstOperand.charAt(x) == '1' && this.secondOperand.charAt(x) == '0' && !this.overflow
                    || this.firstOperand.charAt(x) == '0' && this.secondOperand.charAt(x) == '1' && !this.overflow) {
                this.sum[x + 1] = '1';
                this.overflow   = false;
            } else if (this.firstOperand.charAt(x) == '0' && this.secondOperand.charAt(x) == '0' && this.overflow) {
                this.sum[x + 1] = '1';
                this.overflow   = false;
            } else if (this.firstOperand.charAt(x) == '0' && this.secondOperand.charAt(x) == '0' && !this.overflow) {
                this.sum[x + 1] = '0';
                this.overflow   = false;
            } else { this.sum[x + 1] = '.'; }
        }

        if (overflow && !this.signed) { sum[0] = '1'; }
    }

    public char[] getSum(){ return sum; }

    public static void main(String[] args) {
        Operation operationW = new Operation("1.0100", "0.0101", 5);                // Without GRS
        operationW.performAddition();
        System.out.println(operationW.getSum());

        Operation operationGRS = new Operation("1.011111001", "0.010011111", 10);   // With GRS, add 3 digits for GRS
        operationGRS.performAddition();
        System.out.println(operationGRS.getSum());

        Operation operationN = new Operation("1.000", "-0.111", 4);                 // Negative, needs more checking
        operationN.performAddition();
        System.out.println(operationN.getSum());
    }
}
