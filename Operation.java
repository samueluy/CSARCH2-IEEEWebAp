public class Operation {
    private String firstOperand;
    private String secondOperand;
    private int digits;
    private char[] sum;
    private boolean overflow;
    private boolean signed;

    public Operation(String firstOperand, String secondOperand, boolean grs, int digits) {
        this.firstOperand   = firstOperand;
        this.secondOperand  = secondOperand;
        
        if (!grs) { this.digits = digits + 1; }
        else { this.digits      = (digits + 3) + 1; }
        
        this.sum            = new char[this.digits + 1]; 
        this.overflow       = false;
        this.signed         = false;

        for (int x = 0; x < this.digits + 1; x++) { this.sum[x] = ' '; }
    }
    
    public void performAddition() {
        if (this.firstOperand.charAt(0) == '-') {
            this.firstOperand = String.valueOf(performComplement(this.firstOperand));
            this.signed  = true;
        } else if (this.secondOperand.charAt(0) == '-') {
            this.secondOperand = String.valueOf(performComplement(this.secondOperand));
            this.signed   = true;
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

        if (this.overflow && !this.signed) { this.sum[0] = '1'; }
    }

    public String getSum(){ return String.valueOf(this.sum); }

    private char[] performComplement(String negative) {
        char[] positive  = new char[this.digits];
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
}
