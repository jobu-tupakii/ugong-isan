#include <stdio.h>

int main() {
    int a;
    printf("정수를 입력하세요: ");
    scanf("%d", &a);
    int i=0;
    int sum=0;
    while(i<=a) {
        sum += i;
        i++;
    }
    printf ("%d까지 정수의 합은 %d입니다.", a, sum);
    return 0;
}