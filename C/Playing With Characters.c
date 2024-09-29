#include <stdio.h>

int main()
{
    char ch;
    char s[100];
    char sentence[100];
    scanf("%c", &ch);
    scanf("%s", s);
    scanf("\n");
    scanf("%[^\n]%*c", sentence);
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s", sentence);
    return 0;
}
