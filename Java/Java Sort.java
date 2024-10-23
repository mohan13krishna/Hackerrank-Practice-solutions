import java.util.*;

class Student {
    private int id;
    private String fname;
    private double cgpa;

    public Student(int id, String fname, double cgpa) {
        this.id = id;
        this.fname = fname;
        this.cgpa = cgpa;
    }

    public int getId() {
        return id;
    }

    public String getFname() {
        return fname;
    }

    public double getCgpa() {
        return cgpa;
    }
}

// Complete the code
public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());

        List<Student> studentList = new ArrayList<>();
        while (testCases > 0) {
            int id = in.nextInt();
            String fname = in.next();
            double cgpa = in.nextDouble();
            Student st = new Student(id, fname, cgpa);
            studentList.add(st);
            testCases--;
        }

        // Comparator to sort by CGPA (descending), Name (alphabetical), and ID (ascending)
        Collections.sort(studentList, new Comparator<Student>() {
            @Override
            public int compare(Student s1, Student s2) {
                // Compare by CGPA in descending order
                int cgpaComparison = Double.compare(s2.getCgpa(), s1.getCgpa());
                if (cgpaComparison != 0) {
                    return cgpaComparison;
                }
                // If CGPA is the same, compare by first name in alphabetical order
                int nameComparison = s1.getFname().compareTo(s2.getFname());
                if (nameComparison != 0) {
                    return nameComparison;
                }
                // If both CGPA and name are the same, compare by ID in ascending order
                return Integer.compare(s1.getId(), s2.getId());
            }
        });

        // Print the sorted student names
        for (Student st : studentList) {
            System.out.println(st.getFname());
        }
    }
}
