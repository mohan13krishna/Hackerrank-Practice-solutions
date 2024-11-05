


if ("pizza".equalsIgnoreCase(order)) {
            return new Pizza();
        } else if ("cake".equalsIgnoreCase(order)) {
            return new Cake();
        } else {
            return null; // In case of invalid input, though not specified
        }
   
