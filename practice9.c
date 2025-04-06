#include <stdio.h>

int main() {
    int a;
    printf("양의 정수를 입력하세요: ");
    scanf("%d", &a);
    if (a>=0) {
        if (a%2 == 0)
        printf ("짝수입니다.");
        else printf("홀수입니다.");
    }
    else printf("양의 정수가 아닙니다.");
}