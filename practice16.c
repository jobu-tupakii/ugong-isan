#include <stdio.h>

union Data {
    int intData;
    float floatData;
    char charData;
};

int main() {
    int a;
    union Data d;
    printf("1. 정수 입력\n2. 실수 입력\n3. 문자 입력\n선택하세요: ");
    scanf("%d",&a);
    if (a == 1) {
        printf("정수를 입력하세요: ");
        scanf("%d", &d.intData);
        printf("입력한 값은: %d", d.intData);
    }
    else if (a == 2) {
        printf("실수를 입력하세요: ");
        scanf("%f", &d.floatData);
        printf("입력한 값은: %.2f", d.floatData);
    }
    else {
        printf("문자를 입력하시오: ");
        scanf(" %c", &d.charData);
        printf("입력한 값은: %c", d.charData);
    }
}