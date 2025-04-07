#include <stdio.h>

int main() {
    int arr[10];
    int i;
    int sum1 = 0;
    int sum2 = 0;
    printf("정수 10개를 입력하세요: ");
    for(i=0; i<10; i++) {
        scanf("%d", &arr[i]);
    }
    for(i=0; i<10; i++) {
        if(arr[i]%2==0) {
            sum1 += arr[i];
        }
        else sum2 += arr[i];
    }
    printf("짝수의 합: %d\n", sum1);
    printf("홀수의 합: %d", sum2);
}