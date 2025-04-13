#include <stdio.h>

int main () {
    int arr[100] = {0};
    int i=0;

    printf ("정수를 입력하세요.\n");
    scanf("%d", &i);
    printf ("정수 %i개를 입력하세요: ", i);
    for (int a=0; a < i; a++) {
        scanf("%d", &arr[a]);
    };
    
    int max=arr[0];
    int min=arr[0];
    int max_ad = 0;
    int min_ad = 0;

    for(int b=0; b < i; b++) {
        if (arr[b] > max) {
        max = arr[b];
        max_ad = b;
        }
        if (arr[b] < min) {
        min = arr[b];
        min_ad = b;
        }
    }

    printf("최대값: %d, 위치: %d\n최소값: %d, 위치: %d\n", max, max_ad, min, min_ad);
}