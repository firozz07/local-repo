#include<stdio.h>
#define SIZE 5
int stack[SIZE];
int top=-1;

void pop(void) {
    if (top == -1) {
        printf("stack is empty");
    } else {
        top--;
    }
}
int main(){
    stack[++top]=10;
    stack[++top]=20;
    stack[++top]=30;
    stack[++top]=40;
    stack[++top]=50;
    for(int i=0;i<SIZE;i++){
        printf(" %d",stack[i]);
    }

    pop();
   
    printf("\n");
    for(int i=0;i<=top;i++){
        printf(" %d",stack[i]);
    }
}