#include<stdio.h>
int main(){

    int i, j, a, b,sum = 0;
    printf("enter the number at which you want to add prime numbers\n");
    scanf("%d",&a);

    for(i=2;i<=a;i++){

        b = 1;
        for(j = 2; j <= i/2; j++){

            if(i % j == 0){
                b = 0;
                break;
            }


        }
        if(b == 1){
            sum += i;