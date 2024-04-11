import java.util.Scanner;

public class Menu{
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        boolean i = true;

        while(i){
            System.out.println("-------------------------------------------------------------------");
            System.out.println("1. 환자 등록 | 2. 환자 조회 | 3. 환자 관리 | 4. 환자 삭제 | 5. 종료");
            System.out.println("-------------------------------------------------------------------");

            int input= sc.nextInt();
            sc.nextLine();

            switch (input) {
                case 1:
                    System.out.println("----------------------------");
                    System.out.println("등록할 환자정보를 입력하세요");
                    System.out.println("----------------------------");
                    String name = sc.nextLine();
                    System.out.println(name);       

                    break;

                case 2:
                    System.out.println("-------------");
                    System.out.println("환자정보 조회");
                    System.out.println("-------------");
            
                    DBCon db = new DBCon();
                    db.connect();
                    sc.nextLine();
                    break;

                case 3:
                    break;

                case 4:
                    break;

                case 5:
                    i = false;
                    break;
            
                default:
                    break;
            }
        }
        sc.close();
    }
}