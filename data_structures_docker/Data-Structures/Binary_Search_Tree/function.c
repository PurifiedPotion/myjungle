#include <stdio.h>

// 선언
void p(int num);

int main_function(void)
{
    // function
    // 계산기

    int num = 2;
    printf ("num은 %d 입니다\n", num);

    // 2 + 3은?
    num = num + 3;
    return 0;
}

// 정의
void p(int num)
{
    printf("num은 %d 입니다\n", num);
}