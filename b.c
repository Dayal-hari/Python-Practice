// write a programme to store record of 15 employees using concept of array of structures each employee should enter 3 details employee name , employee sallary , and date of joining 


#include <stdio.h>
#include <string.h>
struct Employee {
    char name[50];
    float salary;
    char dateOfJoining[20]; 
};
int main() {
    struct Employee employees[15]; 
    int i;
    for(i = 0; i < 15; i++) {
        printf("Enter details for Employee %d:\n", i + 1);
        printf("Enter name: ");
        fgets(employees[i].name, sizeof(employees[i].name), stdin);
        employees[i].name[strcspn(employees[i].name, "\n")] = '\0'; 
        printf("Enter salary: ");
        scanf("%f", &employees[i].salary);
        getchar();
        printf("Enter date of joining (DD-MM-YYYY): ");
        fgets(employees[i].dateOfJoining, sizeof(employees[i].dateOfJoining), stdin);
        employees[i].dateOfJoining[strcspn(employees[i].dateOfJoining, "\n")] = '\0'; 

        printf("\n");
    }
    printf("\nEmployee Records:\n");
    printf("----------------------------------------------------------\n");
    printf("No  Name                          Salary   Date of Joining\n");
    printf("----------------------------------------------------------\n");

    for(i = 0; i < 15; i++) {
        printf("%-3d %-30s %-8.2f %-20s\n", i + 1, employees[i].name, employees[i].salary, employees[i].dateOfJoining);
    }

    return 0;
}
