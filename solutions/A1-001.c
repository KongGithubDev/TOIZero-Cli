#include <stdio.h>

int main() {
    char fname[100], lname[100];
    scanf("%s %s", fname, lname);
    printf("Hello %s %s\n", fname, lname);
    printf("%.2s%.2s\n", fname, lname);
    return 0;
}