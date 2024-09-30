#include <stdio.h>

// Function to find the greatest of four numbers 
int max_of_four(int a, int b, int c, int d) 
{ 
    int max = a; 
  
    if (b > max) 
      max = b; 
  
    if (c > max) 
      max = c; 
  
    if (d > max) 
      max = d; 
  
    return max; 
} 
  
// Driver program 
int main() 
{ 
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    printf("%d", max_of_four(a, b, c, d)); 
  
    return 0; 
}
