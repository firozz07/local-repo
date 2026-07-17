public class MultiMatrix {
    public static void main(String[] args) {
        int [][] FirstMatrix = {{2, 3, 4}, {5, 7, 8}};
        int [][] SecondMatrix = {{2, 3, 4}, {5, 7, 8}};

        int rows = FirstMatrix.length;
        int columns = FirstMatrix[0].length;

        if (SecondMatrix.length != rows || SecondMatrix[0].length != columns) {
            System.out.println("Matrices must have the same dimensions for element-wise multiplication.");
            return;
        }

        int [][] product = new int[rows][columns];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                product[i][j] = FirstMatrix[i][j] * SecondMatrix[i][j];
            }
        }

        System.out.println("The multiplication is:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.print(product[i][j] + " ");
            }
            System.out.println();
        }
    }
}
