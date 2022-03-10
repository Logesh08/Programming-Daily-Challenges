// Define class Stick
// The program must accept the length of a stick and Q queries as the input. The query can be any one of the following two types.
// - If the query type is 1, then the program must combine the stick with the given stick of length X (where X is a non-negative integer). If the length of the stick to be combined is 0, then the program must print "Length of the stick cannot be zero".
// - If the query type is 2, then the program must break the stick by dividing the length by 2 only if the length is even. Else the program must print "Length of the stick cannot be odd".
// After performing the operation of each query, the program must print the revised length of the stick.

// Your task is to define the class Stick so that the program runs successfully.

// Example Input/Output 1:
// Input:
// 120
// 5
// 1 15
// 2
// 1 5
// 2
// 1 0

// Output:
// 135
// Length of the stick cannot be odd
// 135
// 140
// 70
// Length of the stick cannot be zero
// 70

// Explanation:
// Initially, the length of the stick is 120.
// 1st query: X = 15. After combining the sticks, the length of the stick becomes 135 (120 + 15).
// 2nd query: The current length of the stick is 135 which is odd. Hence "Length of the stick cannot be odd" and 135 are printed.
// 3rd query: X = 5. After combining the sticks, the length of the stick becomes 140 (135 + 5).
// 4th query: The length of the stick is even. Hence the revised length of the stick is 70.
// 5th query: X = 0. The length of the stick to be combined is 0. Hence "Length of the stick cannot be zero" and 70 are printed.

// Example Input/Output 2:
// Input:
// 40
// 9
// 2
// 2
// 2
// 2
// 1 3
// 2
// 2
// 2
// 2

// Output:
// 20
// 10
// 5
// Length of the stick cannot be odd
// 5
// 8
// 4
// 2
// 1
// Length of the stick cannot be odd
// 1













import java.util.*;
class Stick{
    int length;
    Stick(int len){
        length=len;
    }
    void breakStick(){
        if(length%2!=0){
            System.out.println("Length of the stick cannot be odd");
        }else{
            length = length / 2;
        }
    }
    int getLength(){
        return length;
    }
    void combineStick(Stick s){
        if(s.getLength()==0){
            System.out.println("Length of the stick cannot be zero");
            return;
        }
        this.length += s.getLength();
    }
}
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int stickLen = Integer.parseInt(sc.nextLine());
        Stick stick = new Stick(stickLen);
        int Q = Integer.parseInt(sc.nextLine());
        for (int ctr = 1; ctr <= Q; ctr++) {
            String query[] = sc.nextLine().trim().split("\\s+");
            int queryType = Integer.parseInt(query[0]);
            if (queryType == 1) {
                stick.combineStick(new Stick(Integer.parseInt(query[1])));
            } else if (queryType == 2) {
                stick.breakStick();
            }
            System.out.println(stick.getLength());
        }
    }
}