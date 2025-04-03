#include <stdio.h>

int main() {
    int a;
    printf("정수를 입력하세요: \n");
    scanf("%d", &a);
    if (a%2 == 0) {
        printf("짝수입니다.");
    }
    else
    printf("홀수입니다.");
}
