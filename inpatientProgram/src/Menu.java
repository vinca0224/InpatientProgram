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
                    System.out.println("---------");
                    System.out.println("환자 등록");
                    System.out.println("---------");
                    break;

                case 2:
                DBCon db = new DBCon();
                db.connect();
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
