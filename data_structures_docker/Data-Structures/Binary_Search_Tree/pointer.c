#include <stdio.h>
int main(void)
{
    // 포인터

    // [철수] : 101호
    // [영희] : 201호
    // [민수] : 301호
    // 문 앞에 '암호'가 걸려 있음
    int 철수 = 1; //암호
    int 영희 = 2;
    int 민수 = 3;

    printf("철수네 주소 : %d, 암호 : %d\n", &철수, 철수);


    return 0;
}