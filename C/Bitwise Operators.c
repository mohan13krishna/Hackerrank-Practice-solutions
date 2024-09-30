#include <stdio.h>

int calculate_the_maximum(int n, int k){
    int max_and = 0;
    int max_or = 0;
    int max_xor = 0;
    int i, j;
    for (i = 1; i <= n; i++){
        for (j = i + 1; j <= n; j++){
            if ((i & j) < k && (i & j) > max_and){
                max_and = i & j;
            }
            if ((i | j) < k && (i | j) > max_or){
                max_or = i | j;
            }
            if ((i ^ j) < k && (i ^ j) > max_xor){
                max_xor = i ^ j;
            }
        }
    }
    printf("%d\n", max_and);
    printf("%d\n", max_or);
    printf("%d\n", max_xor);
    return 0;
}

int main(){
    int n, k;
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
    return 0;
}
