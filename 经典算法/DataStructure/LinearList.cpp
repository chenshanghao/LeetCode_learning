#define InitSize 50      //定义线性表的最大长度
typedef struct 
{
    ElemType    *data;
    int MaxSize, length;
} SeqList;

L.data = new ElemType[InitSize];


//插入操作
bool ListInsert(SeqList &L, int i, ElemType e){
    if (i<1 || i>L.length+1)
        return false;
    if (L.length>=MaxSize)
        return false;
    for(int j=L.length; j>=i; j--)
        L.data[j] = L.data[j-1];
    L.data[i-1] = e;
    L.length;
    return true;
}

//删除操作
bool ListDelete(SeqList &L, int i, int &e){
    if(i<1||i>L.length)
        return false;
    e=L.data[i-1]
    for(int j=i; j<L.length; j++)
        L.data[j-1]=L.data[j];
    L.length--;
    return true;
}

// 按值查找
int LocateElem(SeqList L, ElemType e){
    int i;
    for(i=0;i<L.length;i++)
        if(L.data[i]==e)
            return i+1;
    return 0;
}
