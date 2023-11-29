import java.util.Scanner;

public class App11 {
    public static void main(String[] args) {
        int a, b, c;
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println(" Nhap a ");
            a = sc.nextInt();
            System.out.println(" Nhap b ");
            b = sc.nextInt();
            System.out.println(" Nhap c ");
            c = sc.nextInt();
        }
        if (a == 0) {
            if (b == 0 || c == 0 || a == 0) {
                System.out.println(" phuong trinh vo nghiem ");

            } else {
                System.out.println(" phuong trinh vo so nghiem ");
                System.out.println(" phuong trinh co mot nghiem ");
            }
        }
    }
}