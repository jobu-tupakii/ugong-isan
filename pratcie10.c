#include <stdio.h>

int main () {
    int arr[5];
    int i;
    printf("정수를 5개 입력하세요: ");
    for (i=0; i <= 4; i++) {
        scanf("%d", &arr[i]);
    }
    printf("입력하신 숫자는 ");
    for(i=0; i <= 4; i++)
    printf("%d", arr[i]);

    int sum = 0;
    for (i=0; i <= 4; i++) {
        sum += i;
    }

    printf("\n입력하신 숫자의 합은 %d 입니다.", sum);
}