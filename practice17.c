#include <stdio.h>

int main() {
    int arr[100];
    int i;
    int t;
    int a=0, b=0;
    printf("정수를 입력하세요\n");
    scanf("%d", &i);
    for(t=0; t<=i; t++) {
        arr[t] = t;
    }
    for(t=0; t<=i;t++) {
        if(arr[t]/10 == 3) a++;
        if(arr[t]%10 == 3) b++;
    }
    int sum = 0;
    sum = a+b;
    printf("3의 개수: %d\n", sum);
}