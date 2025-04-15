class A {
    public static void display() {
        System.out.print("A");
    }
}

class B extends A {
    public static void display() {
        System.out.print("B");
    }
}

class C extends B {
    public static void display() {
        System.out.print("C");
    }
}

class Test {
    public static void main(String[] args) {
        A obj1 = new A();
        A obj2 = new B();
        A obj3 = new C();
        
        obj1.display();  // 1
        obj2.display();  // 2
        obj3.display();  // 3
    }
}
