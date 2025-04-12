#include <stdio.h>

int main () {
    int i=0;
    printf("양의 정수를 입력하세요.\n");
    scanf("%d", &i);
    if (i > 0) {
        if (i % 2 == 0) printf("짝수입니다.\n");
        else printf("홀수입니다.\n");
    }
    else printf("양의 정수가 아닙니다.\n");
    return 0;
}