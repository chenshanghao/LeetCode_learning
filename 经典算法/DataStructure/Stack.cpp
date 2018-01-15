#define MaxSize 50              //定义栈中元素的最大个数

typedef struct{
    Elemtype data[MaxSize];     //存放栈中元素
    int top;                    //栈顶指针
}SqStack;  

//初始化
void InitStack(&S){
    S.top=-1;
} 

//判栈空
bool StackEmpty(S){
    if(S.top==-1)               //栈空
        return true;
    else                        //不空
        return false;
}

//进栈
bool Push(SqStack &S, Elemtype x){
    if(S.top==MaxSize-1)        //栈满，报错
        return false;
    S.data[++S.top]==x;         //指针先加1，再入栈
    return true;
}

//出栈
bool Pop(SqStack &S, Elemtype &x){
    if(S.top==-1)               //栈空，报错
        return false;       
    x=S.data[S.top--];          //先出栈，指针再减1
    return true;
}

//读栈顶元素
bool GetTop(SqStack S, Elemtype &x){
    if(S.top==-1)
        return false;
    x=S.data[S.top];
    return true;
}

