public class Normalize{
        private String binInput = "";
        private int binExponent = 0;
        public Normalize(Operand operand){
                this.binInput = operand.binary;
                this.binExponent = operand.exponent;
        }

        public void normalize(){
                String binary = getBinInput();
                int exponent = getBinExponent();

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
                                exponent = exponent+(oneLoc-radixLoc);
                        else if (oneLoc < radixLoc)
                                exponent = exponent-((radixLoc-1)-oneLoc);
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
                                exponent = exponent+(oneLoc-radixLoc);
                        else if (oneLoc < radixLoc)
                                exponent = exponent-((radixLoc-1)-oneLoc);
                }

                setBinInput(newBinary.toString());
                setBinExponent(exponent);
        }

        public String getBinInput() {
                return binInput;
        }

        public int getBinExponent() {
                return binExponent;
        }

        public void setBinInput(String binInput) {
                this.binInput = binInput;
        }

        public void setBinExponent(int binExponent) {
                this.binExponent = binExponent;
        }
}

