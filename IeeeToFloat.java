import java.lang.Math;
import java.util.Scanner;
public class IeeeToFloat {
    static float convert(String mantissa_str) {
        int power_count = -1;
        float mantissa_int = 0;
        for (int i = 0; i < mantissa_str.length(); i++) {
            mantissa_int += (Character.getNumericValue(mantissa_str.charAt(i)) * Math.pow(2, power_count));
            power_count -= 1;
        }
        return (mantissa_int + 1);
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Input the sign bit: ");
        int sign_bit = input.nextInt();
        System.out.println("Input the exponent bits: ");
        String exponent_str = input.next();
        int exponent = Integer.parseInt(exponent_str, 2);
        int exponent_prime = exponent - 127;
        System.out.println("Input the mantissa bits: ");
        String mantissa_str = input.next();
        float mantissa_int = convert(mantissa_str);
        float answer = (float) (Math.pow(-1, sign_bit) * mantissa_int * Math.pow(2, exponent_prime));
        System.out.printf("The float value of the given IEEE-754 representation is: %.6f\n", answer);
        input.close();
    }
}