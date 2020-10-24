#include<iostream>
#include<fstream>
#include<algorithm>
#include<list>
#include<iterator>

using namespace std;
int main(){
  list<int>theList;
  ifstream infile("ITER.DAT");

  istream_iterator<int> file_iter(infile);
  istream_iterator<int> end_of_stream;

  copy(file_iter,end_of_stream,back_inserter(theList));

  cout<<endl;
  ostream_iterator<int>ositer(cout," ");
  copy(theList.begin(),theList.end(),ositer);
  cout<<"\nCopied Successfully!"<<endl;
  return 0;
}