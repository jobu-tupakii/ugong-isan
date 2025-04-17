class Example {
    static {
        System.out.println("Static Block");
    }
    static void staticMethod() {
        System.out.println("Static Method");
    }
    Example() {
        System.out.println("Constructor");
    }
}

public class STT01 {
    public static void main(String[] args) {
        Example.staticMethod();
        Example ex = new Example();
        Example.staticMethod();
    }
}
