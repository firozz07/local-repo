

public class BreakContinue {
    public static void main(String[] args) {
        for (int i = 1; i < 100; i++) {
            if(i%2==1) continue;
            if(i==10) break;
            System.out.print(i+" ");
        }
    }
}
