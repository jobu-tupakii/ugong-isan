#include <stdio.h>

int main () {
    int a;
    printf("출력할 구구단 단 수를 입력하세요 : ");
    scanf("%d", &a);
    for(int i=1; i<=9; i++) {
        printf("%d x %d = %d\n", a, i, a*i);
    }
}