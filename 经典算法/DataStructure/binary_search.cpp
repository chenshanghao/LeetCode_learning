int Binary_Search(SeqList L, ElemType key){
    //有序表中查找关键字为key的元素，若存在返回其位置，不存在返回-1
    int low=0,high=L.TableLen-1,mid;
    while(low<=high){
        mid=(low+high)/2;
        if(L.elem[mid]==key)
            return mid;
        else if(L.elem[mid]>key)
            high=mid-1;
        else
            low=mid+1;
    }
    return false;
}