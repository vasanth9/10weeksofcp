#include<bits/stdc++.h>
using namespace std;
int main()
{
  cout<<"Hello World\n";
  string list[]={
    "what to do now?",
    "I want to do many things but nothing goes as planned",
    "so, need to work on basics and also indepth of the languages",
    "Need to concentrate on academics",
    "I like it working on repl.it",
    "What to do next?",
    "The problem is I have  so many in my bucket list and at the same time , it seems I have none"
  };
int i=1;
for (string x:list){
  cout<<i<<".) "<<x<<"\n";i++;
}
}