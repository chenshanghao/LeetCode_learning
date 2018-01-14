//The first solution needs the size of a char and size of two integers, all of which will be allocated from the stack. 
//This solution is the most commonly accepted “good” solution. Here is the code.
void reverseString(char* str)
{
    int i, j;
    char temp;
    i=j=temp=0;

    j=strlen(str)-1;
    for (i=0; i<j; i++, j--)
    {
        temp=str[i];
        str[i]=str[j];
        str[j]=temp;
    }
}

//The second solution is slightly better than the first as it does not need the char space. 
//It uses bitmanipulation (XOR in this case) to swap the chars in place.
void reverseStringBetter(char* str)
{
    int i, j;
    i=j=0;

    j=strlen(str)-1;
    for (i=0; i<j; i++, j--)
    {
        str[i] ^= str[j] ;
        str[j] ^= str[i] ;
        str[i] ^= str[j] ;
    }
}