#include<iostream>
using namespace std;
int main()
{
   int n,flag=0;
   cout<<"enter a no";
   cin>>n;
   for(int i=2;i<n;i++)
   {
     for(int j=2;j<i;j++)
     {
       if(i%j==0)
       flag++;
       break;
     }
   }
   if(flag==1)
   cout<<"prime";
   else
	   cout<<"not prime";
   return 0;
}

