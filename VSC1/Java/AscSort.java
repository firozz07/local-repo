package VSC1.Java;
public class AscSort {
public static void main(String[] args) {
    int [] arr={2,8,9,27};
    for (int i = 0; i < arr.length; i++) {
        for (int j = 0; j < arr.length; j++) {
            if(arr[i]<arr[j]){
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
        
    }
    for(int k:arr) System.out.print(k+" ");
}
}
