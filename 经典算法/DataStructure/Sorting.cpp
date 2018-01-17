
//merge sort  (conquer and divide)
void MergeSort(ElemType A[], int low, int high){
    if(low<high){
        int mid=(low+high)/2;       //从中间划分两个排序
        MergeSort(A,low,mid);       //对左侧子序列进行递归排序
        MergeSort(A,mid+1,high);    //对右侧子序列进行递归排序
        Merge(A,low,mid,high);      //归并
    }
}


ElemType *B=(ElemType *)malloc((n+1)*sizeof(ElemType)); //辅助数组B

void Merge(ElemType A[], int low, int mid, int high){
//A表的两断A[low...mid]和A[mid+1...high]各自有序，将它们合并成一个有序表
    for(int k=low;k<=high;k++)
        B[k]=A[k];              //A的元素复制到B中
    for(i=low, j=mid+1,k=i;i<mid&&j<=high;k++){
        if(B[i]<=B[j])          //比较B的左右两段中的元素
            A[k]=B[i++];        //将较小的值复制到A中
        else
            A[k]=B[j++];
    }//for 只会执行一个
    while(i<=mid)   A[k++]=B[i++];  //若第一个表未检测完，复制
    while(j<high)   A[k++]=B[j++];  //若第二个表未检测完，复制
}


//Quick Sort (conquer and divide)
void QuickSort(ElemType A[], int low, int high){
    if(low<high){           //递归跳出条件
        //partition()就是划分操作，将表A[low...high]划分为两个上述条件的两个子表
        int pivotpos=Partition(A,low,high);     //划分
        QuickSort(A,low,pivotpos-1);            //依次对两个字表进行递归排序
        QuickSort(A,pivotpos+1,high);
    }
}

int Partition(ElemType A[], int low, int high){
    ElemType pivot=A[low];  //将当前表中的第一个元素设为枢轴值，对表进行划分
    while(low<high){        //跳出循环条件
        while(low<high&&A[high]>=pivot)  --high;
        A[low]=A[high];     //比枢轴值小的元素移动到左端
        while(low<high&&A[low]<=pivot)  ++low;
        A[high]=A[low];     //比枢轴值小的元素移动到右端
    }
    A[low]=pivot;
    return low;
}


























