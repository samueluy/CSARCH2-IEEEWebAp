

public class test {
    public static void main(String[] args){

        Operand operand = new Operand("110111.11011111", 10);
        Normalize Main = new Normalize(operand);
        Main.normalize();
    }
}
