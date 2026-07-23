#include<stdio.h>
#define size 5
int top=-1;
int stack[size];

void push(){
     int n,value;
    printf("how much nums you want to add?");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
         if(top==size-1){
        printf("stack is full");
        break;
        }
        else{
        top++;
        printf("enter the num one by one");
        scanf("%d",&value);
        stack[top]=value;
        }
    }
}
void pop(){
    if(top==-1){
        printf("stack is empty");
    }
    else{
        top--; 
    }
   
}

void isempty(){
    if(top==-1){
        printf("the stack is empty");
    }
    else{
        printf("the stack is not empty");
    }
}

void isfull(){
    if(top==size-1){
        printf("the stack is full");
    }
    else{
        printf("the stack is not full");
    }
}
void peek(){
    if(top==-1){
        printf("the stack is empty");
    }
    else{
    printf(" the peek element is %d\n",stack[top]);
    }
}

void display(){
    if(top==-1){
        printf("the stack is empty");
    }
    else{
    for(int i=0;i<=top;i++){
        printf("  %d",stack[i]);
    }
    printf("\n");
}
}
int main(){
int ch;
while (1)
{
    
    printf("enter the number as per the operation  \n");
    printf("1 for the push\n");
    printf("2 for the pop\n");
    printf("3 for the isempty\n");
    printf("4 for the isfull\n");
    printf("5 for the peek\n");
    printf("6 for the displaying element\n");
    printf("0 for the exit\n");
    scanf("%d",&ch);

    switch (ch)
    {
    case 1 :
        push();
        break;
    case 2 :
        pop();
        break;
    case 3 :
        isempty();
        break;
    case 4 :
        isfull();
        break;
    case 5 :
        peek();
        break;
    case 6 :
        display();
        break;
    case 0:
    return 0;
    break;
    default:
    printf("enter correct number ");
        break;
    }
}
}
