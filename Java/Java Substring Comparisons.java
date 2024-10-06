

public static String getSmallestAndLargest(String s, int k) {
if (s.length() < k) {
return "Error: String length is less than k";
}
String smallest = s.substring(0, k);
String largest = smallest;
for (int i = 1; i <= s.length() - k; i++) {
String curr = s.substring(i, i + k);
if (curr.compareTo(smallest) < 0) {
smallest = curr;
}
if (curr.compareTo(largest) > 0) {
largest = curr;
}
}
return smallest + "\n" + largest;
}

