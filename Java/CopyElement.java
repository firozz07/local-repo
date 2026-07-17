package Java;

public class CopyElement {
    public static void main(String[] args) {
        int [] arr={2,3,4,5,6};
        int [] arr2=new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            arr2[i] = arr[i];
        }
        for(int k:arr2) System.out.print(k+" ");
    }
}
