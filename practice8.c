#include <stdio.h>

int main () {
    int i;
    int arr[4] = {};
    for(i = 0; i <=3; i++) {
    printf("%d번째 정수를 입력하세요: ", (i+1));
    scanf("%d", &arr[i]);
    }
    for (i=0; i <= 3; i++) {
    printf("%d",arr[i]);
    }
}