#include <stdio.h>

int main () {
    int i;
    int b;
    printf ("출력할 구구단 단 수를 입력하세요: ");
    scanf ("%d", &i);
    for (int a=0; a <= 9; a++) {
        b = i * a;
        printf("%d * %d = %d\n", i, a, b);
    }
}