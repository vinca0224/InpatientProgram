import java.util.Scanner;

public class Register {
    String name;
    Scanner scIn = new Scanner(System.in);

    String setInfo(){
        System.out.println("이름 입력");
        name = scIn.nextLine();
        return name;
    }

    void getInfo(){
        System.out.println(name);
    }
}
