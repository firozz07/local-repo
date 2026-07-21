#include<stdio.h>
#define size 5
int stack[size];
int top=-1;
int full(value){
    if(top==size-1){
        return 1;
    }
    else{
        return 0;
    }
}
int main(){
    stack[++top]=10;
    stack[++top]=20;
    stack[++top]=30;
    stack[++top]=40;
    stack[++top]=50;
    

    printf(full()==1?" the stack is full " : "the stack is not full");
    printf("heres the stack : \n");
    for(int i=0;i<=top;i++){
        printf("  %d",stack[i]);
    }

}