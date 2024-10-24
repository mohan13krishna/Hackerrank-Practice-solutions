
import java.util.PriorityQueue; // Add this import statement


class Student implements Comparable<Student> {
    int id;
    String name;
    double cgpa;

    public Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getCgpa() {
        return cgpa;
    }

    @Override
    public int compareTo(Student other) {
        if (Double.compare(cgpa, other.cgpa) != 0) {
            return Double.compare(other.cgpa, cgpa); // Reverse order for higher CGPA priority
        } else if (!name.equals(other.name)) {
            return name.compareTo(other.name);
        } else {
            return Integer.compare(id, other.id);
        }
    }

    @Override
    public String toString() {
        return name;
    }
}

class Priorities {
    private PriorityQueue<Student> studentQueue = new PriorityQueue<>();

    public void enqueue(Student student) {
        studentQueue.offer(student);
    }

    public Student dequeue() {
        return studentQueue.poll();
    }

    public List<Student> getStudents(List<String> events) {
        for (String event : events) {
            String[] parts = event.split(" ");
            if (parts[0].equals("ENTER")) {
                String name = parts[1];
                double cgpa = Double.parseDouble(parts[2]);
                int id = Integer.parseInt(parts[3]);
                enqueue(new Student(id, name, cgpa));
            } else if (parts[0].equals("SERVED")) {
                dequeue();
            }
        }

        List<Student> students = new ArrayList<>();
        while (!studentQueue.isEmpty()) {
            students.add(dequeue());
        }
        return students;
    }
}


