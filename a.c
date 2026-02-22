#include <stdio.h>
struct emp
{
    int id;
    char name[36];
    float sal;
};
int main()
{
    struct emp e;
    int clrscr();
    printf("enter employee id , name , salary :");
    scanf("%d",&e.id);
    scanf("%s",&e.name);
    scanf("%f",&e.sal);
    printf("Id: %d",e.id);
    printf("\nName: %s",e.name);
    printf("\nSalary: %f",e.sal);
   int getch();
}