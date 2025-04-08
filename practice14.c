#include <stdio.h>

struct Student {
    char name [20];
    int age;
    int id;
};

int main() {
    int i;
    struct Student s[3];
    for (int i=0; i<3; i++) {
        printf("학생 %d 정보 입력: \n", i+1);
        printf("이름: ");
        scanf("%s", s[i].name);
        printf("나이: ");
        scanf("%d", s[i].age);
        printf("학번: ");
        scanf("%d", s[i].id);
    }
    printf("\n[입력한 학생 정보 출력]\n");
    for (i=0; i<3; i++) {
        printf("이름: %s, 나이: %d, 학번: %d\n", s[i].name, s[i].age, s[i].id);
    }
}