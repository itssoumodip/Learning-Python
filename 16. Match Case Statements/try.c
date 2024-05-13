#include <stdio.h>
int main()
{
    int n;
    printf("Enter your x Input : ");
    scanf("%d", &n);
    switch (n)
    {
        case 0:
          printf("The No is 0");
          break;
        case 5:
          printf("The No is 5");
          break;
        default: 
          printf("This is Default");
    }
    return 0;
}