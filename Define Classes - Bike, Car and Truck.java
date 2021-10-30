// Define Classes - Bike, Car and Truck
// Please define the classes Bike, Car and Truck so that the program prints the following as the output.

// Program's Output:
// Bike
// 2
// Car
// 4
// Truck
// 6



import java.util.*;

interface Vehicle {

    public String getName();

    public int getNumberOfWheels();

} // End of Vehicle interface
class Bike implements Vehicle
{
    private String name = "Bike";
    private int wheels = 2;
    public String getName()
    {
        return this.name;
    }
    public int getNumberOfWheels()
    {
        return this.wheels;
    }
}
class Car implements Vehicle
{
    private String name = "Car";
    private int wheels = 4;
    public String getName()
    {
        return this.name;
    }
    public int getNumberOfWheels()
    {
        return this.wheels;
    }
}
class Truck implements Vehicle
{
    private String name = "Truck";
    private int wheels = 6;
    public String getName()
    {
        return this.name;
    }
    public int getNumberOfWheels()
    {
        return this.wheels;
    }
}
public class Hello {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Vehicle bike = new Bike();
        Vehicle car = new Car();
        Vehicle truck = new Truck();
        System.out.println(bike.getName());
        System.out.println(bike.getNumberOfWheels());
        System.out.println(car.getName());
        System.out.println(car.getNumberOfWheels());
        System.out.println(truck.getName());
        System.out.println(truck.getNumberOfWheels());
    } // End of main function
} // End of Hello class