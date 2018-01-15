//单链表定义
typedef struct LNode{
    ElemType data;
    struct LNode *next;
}LNode, *LinkList;

//头插法建立单链表
LinkList CreatList1(LinkList &L){   //传引用
    //从表尾到表头逆向建立单链表L,每次均在头结点之后插入元素
    LNode   *s; int x;
    L=(LinkList)malloc(sizeof(LNode));  //创建头结点
    L->next=NULL;                       //初始为空链表
    scanf("%d",&x);                     //输入结点的值
    while(x!=9999){                     //输入9999表示结束
        s=(Lnode*)malloc(sizeof(LNode));//创建新结点
        s->data=x;                      
        s->next=L->next;
        L->next=s;
        scanf("%d",&x);
    }

}

//尾插法建立单链表
LinkList CreatList2(LinkList &L){
    //从表头到表尾正向建立单链表L，每次均在表尾插入元素
    int x;      //设元素类型为整型
    L=(LinkList)malloc(sizeof(LNode));  
    LNode *s,*r=L;      //r为表尾指针
    scanf("%d",&s);     //输入结点的值
    while(x!=9999){
        s=(LNode*)malloc(sizeof(LNode));
        s->data=x;
        r->next=s;      //r指向新的表尾结点
        r=s;
        scanf("%d",&x);
    }
    r->next=NULL
    return L;
}

//按序号查找节点值
LNode *GetElem(LinkList L, int i){
    //本算法取出单链表L(带头结点)中的第i个位置的结点指针
    int j=1;
    LNode *p=L->next;
    if(i==0)
        return L;
    if(i<1)
        return NULL;
    while(p&&j<i){
        p=p->next;
        j++;
    }
    return p;
}

//按值查找表结点
LNode *LocateElem(LinkList L, ElemType e){
    Lnode *p=L->next;
    while(p!=NULL&&p->data!=e)
        p=p->next;
    return p
}































