#include <stdio.h>

int main() {
    int a;
    int b;
    int i;
    int arr[10] ={0};
    int count=0;
    int t;
    printf("정수를 입력하세요\n");
    scanf("%d", &a);
    for(i=0; i<=a; i++) {
        printf("%d", i);
    }
    for(i=0; i<=a; i++) {
        t=i;
        do{
            b = t % 10;
            arr[b] ++;
            t = t / 10;
        } while(t != 0);
    }
    printf("\n");
    for(i=0; i<=9; i++) {
        printf("%d ", arr[i]);
    }
}