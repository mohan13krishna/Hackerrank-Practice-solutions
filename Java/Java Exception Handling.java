


class MyCalculator {
    /*
    * Create the method long power(int, int) here.
    */
    public long power(int n, int p) throws Exception {
        // Check if both n and p are zero
        if (n == 0 && p == 0) {
            throw new Exception("n and p should not be zero.");
        }
        // Check if either n or p is negative
        if (n < 0 || p < 0) {
            throw new Exception("n or p should not be negative.");
        }
        // Calculate the power and return it
        return (long) Math.pow(n, p);
    }
}
