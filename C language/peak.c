#include<stdio.h>
#define size 5
int stack[size];
int top=-1;

void push(int values){
    if(top==size-1){
        printf("stack is full");
    }
    else{
        top++;
        stack[top]=values;
        
    }
}
int peak(){
    if(top==-1){
        printf("stack is underflow");
    }
    else{
        return stack[top];
    }
}
int main(){
    push(10);
    printf("%d",peak());
}