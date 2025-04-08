#include <stdio.h>

struct Student {
    char name[20];
    int age;
    int id;
};

int main() {
    struct Student s;
    printf("학생 정보 입력: \n");
    printf("이름: ");
    scanf("%s", s.name);
    printf("나이: ");
    scanf("%d", &s.age);
    printf("학번: ");
    scanf("%d", &s.id);

    printf("\n[입력한 학생 정보 출력]\n");
    printf("이름: %s, 나이: %d, 학번: %d", s.name, s.age, s.id);
}
