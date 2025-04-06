#include <stdio.h>

int main() {
    int arr[5];
    int max;
    printf("정수 5개를 입력하세요: ");
    for(int i=0; i<=4; i++) {
        scanf("%d", &arr[i]);
    }
    max = arr[0];
    for(int i=0; i<=4; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    printf("%d", max);
}