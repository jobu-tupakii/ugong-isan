#include <stdio.h>

int main () {
    int i;
    int a=0;
    int sum=0;
    printf("정수를 입력하세요:\n");
    scanf("%d", &i);
    while(a <= i) {sum += a; a++;};
    printf("1부터 %d까지의 합은 %d입니다.", i, sum);
}