#include<iostream>
#include<string.h>
using namespace std;
int main()
{
   char stri[];
   cout<<"enter the string";
   cin>>stri[];
   int l=0,h=strlen(stri)-1;
   while(h>l)
{
   if(stri[l++]!=stri[h--])
  {
   cout<<"not pelindrome";
  }
else
 cout<<"pelindrom";
}
return 0;
}

