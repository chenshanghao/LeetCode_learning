//sequence Storage
#define MaxSize 50
typedef struct 
{
    ElemType    data[MaxSize];  //定义队列中元素的最大个数
    int front,rear;             //定义队列的队头和队尾指针;
}Squeue;


//循环队列
//初始时:
Q.front=Q.rear=0;
//队首指针进1：
Q.front=(Q.front+1)%MaxSize;
//队尾指针进1:
Q.rear=(Q.rear+1)%MaxSize;
//队列长度:
(Q.rear+MaxSize-Q.front)%MaxSize;
//判断队空条件:
Q.front=Q.rear;


//初始化
void InitQueue(&Q){
    Q.rear=Q.font=0;        //初始化队首,对尾指针
}

//判队空
bool isEmpty(Q){
    if(Q.rear==Q.front) return true;
    else    return false;
}

//入队
bool EnQueue(SqQueue &Q, ElemType x){
    if((Q.rear+1)%MaxSize==Q.front) return false;   //队满
    Q.data[Q.rear]=x;
    Q.rear=(Q.rear+1)%MaxSize;                      //尾指针加1取模
    return  true;
}

//出队
bool DeQueue(Squeue &Q, ElemType &x){
    if(Q.rear==Q.front) return false;               //队空，报错
    x=Q.data[Q.front];
    Q.front=(Q.front+1)%MaxSize;                    //队头指针加1取模
    return true;
}



//队列的链式存储
typedef struct                              //链式队列结点
{
    ElemType    data;
    struct  LinkNode  *next;
}LinkNode;
typedef struct                              //链式队列
{
    LinkNode    *front, *rear;              //队列的队头和队尾指针
}LinkQueue;

//初始化
void  InitQueue(LinkQueue   &Q){
    Q.front=Q.rear=(LinkNode*)malloc(sizeof(LinkNode)); //建立头结点
    Q.front->next=NULL;                                 //初始为空
}

//判断队空
bool isEmpty(LinkQueue  Q){
    if(Q.front==Q.rear) return  true;
    else    return  false;
}

//入队
void    EnQueue(LinkQueue  &Q,ElemType x ){
    s=(LinkNode*)malloc(sizeof(LinkNode));
    s->data=x;  s->next=NULL;               //创建新结点，插入到链尾
    Q.rear->next=s;
    Q.rear=s;
}

//出队
bool DeQueue(LinkQueue &Q,  ElemType x){
    if(Q.front==Q.rear) return false;   //空队
    p=Q.front->next;
    x=p->data;
    Q.front->next=p->next;
    if(Q.rear==p)
        Q.rear=Q.front;                 //若元队列中只有一个结点，删除后变空
    free(p);
    return  true;
}

































