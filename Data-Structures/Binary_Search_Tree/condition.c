#include <stdio.h>

int main_condition(void)
{
    // 버스를 탄다고 가정. 학생 / 일반인으로 구분 (일반인 : 20세)
    int age = 15;
    if(age >= 20)
        printf("일반인 입니다\n");
    else
        printf("학생입니다\n");
    
    // 초등학생(8~13) / 중학생(14~16) / 고등학생(17~19)으로 나누면?
    // if / else if / else
    int age = 8;
    if (age >= 8 && age <= 13)
    {
        printf("초등학생입니다\n");
    }
    else if (age >= 14 && age <= 16)
    {
        printf("중학생입니다\n");
    }
    else if (age >= 17 && age <= 19)
    {
        printf("고등학생입니다\n");
    }
    else
    {
        printf("학생이 아닌가봐요\n");
    }

    // break / continue
    // 1번부터 30번까지 있는 반에서 1번에서 5번까지 조별 발표를 합니다.

    for (int i = 1; i <=30; i++)
    {
        if (i >= 6)
        {
            printf("나머지 학생은 집에 가세요\n");
            break;
        }
        printf("%d번 발표\n", i);
    }

    // 1번부터 30번까지 있는 반에서 7번 학생은 아파서 결석
    // 7번을 제외하고 6번부터 10버까지 조별 발표를 하세요
    for (int i = 1; i <= 30; i++)
    {
        if(i >= 6 && i <= 10)
        {
            if(i == 7)
            {
                continue;
            }
            printf("%d 번 학생은 조별 발표 준비를 하세요\n", i);
        }
    }

    // random

    printf("난수 초기화 이전..\n");
    for(int i=0; i<10; i++)
        printf("%d", rand() % 10);

    srand(time(NULL)); // 난수 초기화
    printf("난수 초기화 이후..\n");
    for(int i=0; i<10; i++)
        printf("%d", rand() % 10);    

    return 0;

    // Up and Down
    srand(time(NULL));
    int num = rand() % 100 + 1; // 1 ~ 100 사이의 숫자
    printf("숫자 : %d\n", num);
    int answer = 0; // 정답
    int chance = 5; // 기회
    while (chance > 0)
    {
        printf("남은 기회 %d 번\n", chance--);
        printf("숫자를 맞혀보세요 (1~100) : ");
        scanf_s("%d", &answer);

        if (answer > num)
        {
            printf("DOWN \n\n");
        }
        else if (answer < num)
        {
            printf("UP \n\n");
        }
        else if (answer == num)
        {
            printf("정답입니다! \n\n");
            break;
        }
        else
        {
            printf("알 수 없는 오류가 발생했어요\n\n");
        }
    }

}