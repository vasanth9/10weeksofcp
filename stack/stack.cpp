#include<bits/stdc++.h>
using namespace std;
int main()
{
    stack<int> S;
cout<<"push syntax: 0 pushvalue\npop syntax:-1\ntop syntax:1\nexit syntax:404\n";
int input,value;
   while(input!=404)
   {
      cin>>input;
      if(input==0){
          cin>>value;
          S.push(value);
      }
      else if(input==-1)
      {
          if(S.empty())
          {
              cout<<"stack is empty()\n";
          }
          else{
              S.pop();
          }
      }
      else if(input==1)
      {
          cout<<S.top()<<"\n";
      }
      else if(input!=404)
      {
          cout<<"enter valid option.\n";
      }
   }
}