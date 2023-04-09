public class PostNormalize {
    private String sum;
    private int exponent;
    private int digits;

    public PostNormalize(String sum, int exponent, int digits) {
        if (sum.charAt(0) == ' ') {
            char[] adjustedSum = new char[sum.length()];

            for (int x = 0; x < sum.length() - 1; x++) { adjustedSum[x] = sum.charAt(x + 1); }

            this.sum = String.valueOf(adjustedSum);
        } 
        else { this.sum = sum; }
        
        this.exponent = exponent;
        this.digits = digits + 1;
    }

    public void performShift() {
        if (this.sum.charAt(1) != '.') {
            char[] normalizedSum = new char[this.sum.length()];
            int y = 0;

            for (int x = 0; x < this.sum.length(); x++) {
                if (x == 1) { normalizedSum[x] = '.'; }
                else if (this.sum.charAt(y) == '.') {
                    x--;
                    y++;
                } else {
                    normalizedSum[x] = this.sum.charAt(y);
                    y++;
                }  
            }

            this.sum = String.valueOf(normalizedSum);
            this.exponent += 1;
        }
    }

    public void performRound() {
        char[] roundedSum = new char[this.digits];
        int x = 0;

        while (x < this.digits) {
            roundedSum[x] = this.sum.charAt(x);
            x++;
        }

        if (this.sum.length() > x) { if (this.sum.charAt(x) == '1') { roundedSum = roundUp(roundedSum); } }

        this.sum = String.valueOf(roundedSum);
    }

    public String getSum() { return this.sum; }

    public int getExponent() { return this.exponent; }

    private char[] roundUp(char[] roundedSum) {
        boolean overflow = true;

        for (int x = this.digits - 1; x > 0 && overflow; x--) {
            if (roundedSum[x] == '1' && overflow) { roundedSum[x] = '0'; } 
            else if (roundedSum[x] == '0' && overflow) {
                roundedSum[x] = '1';
                overflow = false;
            }
        }

        return roundedSum;
    }
}
