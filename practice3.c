#include <stdio.h>

int main() {
    int a;
    printf("2의 보수 문제를 풀어봅시다\n");
    printf("숫자를 입력하세요: \n");
    scanf("%d", &a);
    int rst = ~a + 1;
    int b;
    printf("입력한 숫자의 2의 보수를 입력하세요: \n");
    scanf("%d", &b);
    if (rst == b) {
        printf("정답입니다!");
    }
    else
    printf("틀렸습니다.");
}
