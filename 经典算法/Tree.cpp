//Root: The top node in a tree.
//Child: A node directly connected to another node when moving away from the Root.
//Parent: The converse notion of a child.
//Siblings: A group of nodes with the same parent.
//Descendant: A node reachable by repeated proceeding from parent to child.
//Ancestor: A node reachable by repeated proceeding from child to parent.
//Leaf: (less commonly called External node) A node with no children.
//Internal node: A node with at least one child.
//Degree: The number of subtrees of a node.
//Edge: The connection between one node and another.
//Path: A sequence of nodes and edges connecting a node with a descendant.
//Level: The level of a node is defined by 1 + (the number of connections between the node and the root).
//Height of node: The height of a node is the number of edges on the longest path between that node and a leaf.
//Height of tree: The height of a tree is the height of its root node.
//Depth: The depth of a node is the number of edges from the tree's root node to the node.
//Forest: A forest is a set of n ≥ 0 disjoint trees.


// define Binary tree 定义二叉树
typedef struct BitNode
{
    ElemType    data;
    struct BitNode *lchild, *rchild;
}BitNode, *BiTree;


// preorder tree 先序遍历
void PreOrder(BiTree T){
    if(T != NULL){
        visit(T);
        PreOrder(T->lchild);
        PreOrder(T->rchild);
    }
}

// Inorder 中序遍历
void InOrder(BiTree T){
    if(T != NULL){
        InOrder(T->lchild);
        visit(T);
        InOrder(T->rchild);
    }
}

// not iterative in order
void InOrder2(BiTree T){
    InitStack(S); BiTree p = T;     //初始化栈，p是遍历指针
    while(p||!IsEmpty(S)){          //栈不空或p不空时循环
        if (p){                     //根指针进栈，遍历左子树
            Push(S, p);             //每遇到非空二叉树先向左走
            p = p -> lchild;
        }else{                      //根指针退栈，访问根结点，遍历右子树
            Pop(S,p); visit(p);     //退栈，再访问根结点，遍历右子树
            p = p->rchild;          //再向右子树走
        }
    }
}

// PostOrder 后序遍历
void PostOrder(BiTree T){
    if (T != NULL){
        PostOrder(T->lchild);   //递归遍历左子树
        PostOrder(T->rchild);   //递归遍历右子树
        visit(T);               //访问根节点
    }
}

// 层次遍历(BFS Breadth First Search)
void LevelOrder(BiTree T){
    InitQueue(Q);                       //初始化辅助队列
    BiTree p;   
    EnQueue(Q,p);                       //根结点入队
    while(!IsEmpty(Q)){                 //队列不空循环
        DeQueue(Q,p);                   //队头元素出队
        visit(p);                       //访问当前p所指向结点
        if(p->lchild!= NULL){           
            EnQueue(Q, p->lchild);      //左子树不空，则左子树入队
        }
        if(p->rchild!=NULL){
            EnQueue(Q, p->rchild);      //右子树不空，则右子树入队
        }
    }

}

























