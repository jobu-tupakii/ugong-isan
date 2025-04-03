#include <stdio.h>
int main() {
    int a = 6;
    int b = 5;
    int result = (a & b) | (~a); printf("result: %d\n", result); return 0;
    }