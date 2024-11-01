import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            // Read two inputs, expecting integers
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            
            // Perform division and print the result
            int result = a / b;
            System.out.println(result);
            
        } catch (InputMismatchException e) {
            // Handle the case where the input is not an integer
            System.out.println("java.util.InputMismatchException");
            
        } catch (ArithmeticException e) {
            // Handle the case where there is an arithmetic exception (e.g., division by zero)
            System.out.println("java.lang.ArithmeticException: / by zero");
            
        } catch (Exception e) {
            // Handle any other exceptions
            System.out.println(e);
            
        } finally {
            // Close the scanner
            scanner.close();
        }
    }
}
