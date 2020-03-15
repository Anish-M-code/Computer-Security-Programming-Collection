
/* This C Program was developed by M.Anish to demonstrate Buffer Overflow Vulnerability in C */

//For use in Linux based os only. Recommended GCC or Clang C compiler.

#include<stdlib.h>
#include<stdio.h>

int main()
{
char buffer[10];
printf("Enter string:");

//if the amount of characters entered is more than 10 buffer overflow! gets() will not prevent this flaw.
//Segmentation fault will be displayed.

gets(buffer);
printf("\nThe string stored in buffer is: %s\n",buffer);
return 0;
}

