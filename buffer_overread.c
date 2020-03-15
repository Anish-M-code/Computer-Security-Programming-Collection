
/* This C Program was developed by M.Anish to demonstrate Buffer Overread Vulnerability in C */

//For use in Linux based os only. Recommended GCC or Clang C compiler.

#include<stdlib.h>
#include<stdio.h>
#include<string.h>

int main()
{
char buffer[10];
char secret[10];
int size,i;

//Just give input for string and index of string as -7 and see buffer overread read your dirty secrets.
strcpy(secret,"topsecret");
printf("Enter string:");
scanf("%s",buffer);
printf("Enter index of string to be printed from:");
scanf("%d",&size);
printf("\nThe string stored in buffer is: ");
for(i=size;buffer[i]!='\0';i++)
    printf("%c",buffer[i]);
return 0;
}


