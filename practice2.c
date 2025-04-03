#include <stdio.h>

int main() {
    int a;
    printf("숫자를 입력하세요: ");
    scanf("%d", &a);
    int rst = ~a + 1;
    printf("입력하신 수의 2의 보수는 %d이다.", rst);
}
