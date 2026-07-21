#include<stdio.h>
#define SIZE 5
int stack[SIZE];
int top=-1;

void push(int values){
    if(top==SIZE-1){
        printf("stack is full");
    }
    else{
        top++;
        stack[top]=values;
        
    }
}
int main(){
    push(10);
    push(20);
    push(30);
    push(40);
    push(50);

    for(int i=0;i<SIZE;i++){
        printf("  %d",stack[i]);
    }
    return 0;
}