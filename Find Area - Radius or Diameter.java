// Find Area - Radius or Diameter
// The program must accept an integer Q as the input. If the value of Q is 1, then the radius of a circle is passed as the input. If the value of Q is 2, then the diameter of a circle is passed as the input. The program must print the area of the circle with the precision up to 2 decimal places as the output.

// Your task is to fill in the missing lines of code in the class Circle so that the program runs successfully.

// Example Input/Output 1:
// Input:
// 1
// 5

// Output:
// 78.57

// Explanation:
// Here the value of Q is 1 and the radius of a circle is 5.
// The area of the circle with the precision up to 2 decimal places is 78.57 ((22/7) * 5 * 5).

// Example Input/Output 2:
// Input:
// 2
// 7.5

// Output:
// 44.20






import java.util.*;

class Circle {

    private double radius;

    public Circle(int radius) {
        this.radius = radius;
    }
    int doubleSet = 0;
    public Circle(double radius){
        doubleSet = 1;
        this.radius=radius;
    }
    
    public double getArea(){
        if(doubleSet==1){
            radius/=2.00;
        }
        return radius*radius*(22/7.00);
    }
    

} // end of Circle class

public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int Q = Integer.parseInt(sc.nextLine().trim());
        Circle circle = null;
        if (Q == 1) {
            int radius = Integer.parseInt(sc.nextLine().trim());
            circle = new Circle(radius);
        } else if (Q == 2) {
            double diameter = Double.parseDouble(sc.nextLine().trim());
            circle = new Circle(diameter);
        }
        System.out.print(String.format("%.2f", circle.getArea()));
    } // end of main function
} // end of Hello class