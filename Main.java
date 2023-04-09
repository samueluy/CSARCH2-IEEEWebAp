import java.util.Scanner;

public class Main{

        private String binInput = "";
        private int binExponent = 0;
        private String base2Input = "";
        private int base2Exponent = 0;
        private int digitsSupported = 0;

        private void askForInput(){
                Scanner input = new Scanner(System.in);
                setBinInput(input.next()); // binary input
                setBinExponent(input.nextInt()); // x2 ^ ? of binary input
                setBase2Input(input.next()); // base-2 input
                setBase2Exponent(input.nextInt()); // x2 ^ ? of base-2 input
                // add input for GRS or rounding
                setDigitsSupported(input.nextInt()); // number of digits supported
        }

        public void normalize(String binary, int binExponent, int numOfDigits){
                StringBuilder newBinary = new StringBuilder(binary);
                int radixLoc;
                int oneLoc;
                // look for the decimal point
                for(radixLoc=0; radixLoc<binary.length(); radixLoc++) {
                        if (binary.charAt(radixLoc) == '.') // if found radix
                                break;
                }

                // look for first 1
                for(oneLoc=0; oneLoc<binary.length(); oneLoc++){
                        if(binary.charAt(oneLoc) == '1')
                                break;
                }

                if(binary.charAt(0) == '-'){ // if value is negative
                        newBinary.deleteCharAt(radixLoc);
                        if(oneLoc > 0){
                                if(radixLoc<oneLoc)
                                        newBinary.delete(1, oneLoc-1); // trim zeroes at the start
                                else
                                        newBinary.delete(1, oneLoc); // trim zeroes at the start
                        }
                        newBinary.insert(2,'.'); // add radix point after first 1

                        // modify exponent value
                        if(radixLoc < oneLoc)
                                binExponent = binExponent+(oneLoc-radixLoc);
                        else if (oneLoc < radixLoc)
                                binExponent = binExponent-((radixLoc-1)-oneLoc);

                        // delete
                        System.out.println(newBinary + " " + binExponent);
                }
                else{
                        // generate new string
                        newBinary.deleteCharAt(radixLoc); // delete radix point
                        if(oneLoc > 0){
                                if(radixLoc<oneLoc)
                                        newBinary.delete(0, oneLoc-1); // trim zeroes at the start
                                else
                                        newBinary.delete(0, oneLoc); // trim zeroes at the start

                        }

                        newBinary.insert(1,'.'); // add radix point after first 1

                        // modify exponent value
                        if(radixLoc < oneLoc)
                                binExponent = binExponent+(oneLoc-radixLoc);
                        else if (oneLoc < radixLoc)
                                binExponent = binExponent-((radixLoc-1)-oneLoc);

                        // delete
                        System.out.println(newBinary + " " + binExponent);
                }

        }

        public static void main(String[] args){

        }

        public void setBinInput(String binInput) {
                this.binInput = binInput;
        }

        public void setBinExponent(int binExponent) {
                this.binExponent = binExponent;
        }

        public void setBase2Input(String base2Input) {
                this.base2Input = base2Input;
        }

        public void setBase2Exponent(int base2Exponent) {
                this.base2Exponent = base2Exponent;
        }

        public void setDigitsSupported(int digitsSupported) {
                this.digitsSupported = digitsSupported;
        }
}

