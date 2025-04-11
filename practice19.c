#include <stdio.h>

int main () {
    int a;
    int i;
    int b=0;
    int c=0;

    printf("정수를 입력하세요.\n");
    scanf("%d", &a);
    for (i=1; i <=a; i++) {
        if (i % 2 ==0) b++;
        else c++;
    }
    printf("짝수 개수: %d \n홀수 개수: %d\n", b, c);
}