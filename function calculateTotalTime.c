// function calculateTotalTime
// The function/method calculateTotalTime accepts an argument str. The string str contains multiple integers separated by a space, where each integer ends with a character denoting the unit of time.
// d indicates days.
// h indicates hours.
// m indicates minutes.
// s indicates seconds.

// The function/method calculateTotalTime must return the total time in days, hours, minutes and seconds.

// Your task is to implement the function calculateTotalTime so that the program runs successfully.

// The following structure is used to represent the Time and is already defined in the default code (Do not write this definition again in your code).
// struct Time
// {
//     int days;
//     int hours;
//     int minutes;
//     int seconds;
// };
// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 2h 1d 50m 102s 5d 30s 70m

// Output:
// 6 4 2 12

// Explanation:
// 2h -> 2 hours
// 1d -> 1 day
// 50m -> 50 minutes
// 102s -> 102 seconds
// 5d -> 5 days
// 30s -> 30 seconds
// 70m -> 70 minutes
// Total time: 6 days, 4 hours, 2 minutes and 12 seconds.

// Example Input/Output 2:
// Input:
// 15d 500s 30h 60s

// Output:
// 16 6 9 20








#include <stdio.h>
#include <stdlib.h>

struct Time
{
    int days;
    int hours;
    int minutes;
    int seconds;
};
#include<string.h>
struct Time* calculateTotalTime(char *str)
{
    struct Time *totaltime=malloc(sizeof(struct Time));
    char *ptr=strtok(str," ");
    int day=0,hrs=0,min=0,sec=0;
    while(ptr!=NULL)
    {
        if(ptr[strlen(ptr)-1]=='d')day+=atoi(ptr);
        else if(ptr[strlen(ptr)-1]=='h')hrs+=atoi(ptr);
        else if(ptr[strlen(ptr)-1]=='m')min+=atoi(ptr);
        else sec+=atoi(ptr);
        ptr=strtok(NULL," ");
    }
    if(sec%60>=0)
    {
        min+=sec/60;
        sec=sec%60;
    }
    if(min%60>=0)
    {
        hrs+=min/60;
        min=min%60;
    }
    if(hrs%24>=0)
    {
        day+=hrs/24;
        hrs=hrs%24;
    }
    totaltime->days=day;
    totaltime->hours=hrs;
    totaltime->minutes=min;
    totaltime->seconds=sec;
    return totaltime;
}
int main()
{
    char str[101];
    scanf("%[^\n]", str);
    struct Time *time = calculateTotalTime(str);
    if(time == NULL)
    {
        printf("Time is not formed\n");
    }
    printf("%d %d %d %d", time->days, time->hours, time->minutes, time->seconds);
    return 0;
}