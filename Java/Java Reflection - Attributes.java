

public class Solution {

    public static void main(String[] args) {
        // Get the Class object for the Student class
        Class<?> student = Student.class; // Complete this line

        // Get all declared methods of the Student class
        Method[] methods = student.getDeclaredMethods(); // Complete this line

        // Create a list to store method names
        ArrayList<String> methodList = new ArrayList<>();
        
        // Add all method names to the list
        for (Method method : methods) { // Complete this line
            methodList.add(method.getName()); // Complete this line
        }
        
        // Sort the method names alphabetically
        Collections.sort(methodList);
        
        // Print all method names
        for (String name : methodList) {
            System.out.println(name);
        }
    }
}
