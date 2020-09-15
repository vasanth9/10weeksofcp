/*You are given a binary string, (string which contains 0's and 1's), You have to perform several operations on this string, in one operation choose a non-empty even length substring containing only 0's or only 1's and remove it from the string.

Your goal is to minimize the final length of the string after performing several operations.It is possible that the final string may become empty, in that case print "KHALI" without quotes.

And it can be proved that there is always an unique string with minimal length after performing the operations.

Input:

    First line of input contains an intger T denoting number of testcases.
    Next T lines of input contains a binary string S.

Output:

    for each testcase print the required minimal string.

Constraints:

    1 <= T <= 10
    1 <= |S|  <= 105
    input:
    2
    101001
    1001   
    output:
    10
    KHALI
*/

#include<bits/stdc++.h>
using namespace std;
int main()
{
    stack<char>initial;
    int n;
    string s;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>s;
        int l=s.length();
        for(int j=0;j<l;j++)
        {
           initial.push(s[j]);
        }
       

    
   stack<char>help;
   while(!initial.empty())
   {
       if(help.empty())
       {  
           help.push(initial.top());
           initial.pop();
           if(initial.top())
           {
               break;
           }
       }
       if(help.top()==initial.top())
       {
           help.pop();
           initial.pop();
       }
       else{
           help.push(initial.top());
           initial.pop();
       }
   }
   if(help.empty())
   {
       cout<<"KHALI\n";
   }
   else{
       while(!help.empty())
       {
           cout<<help.top();
           help.pop();
       }
   }
    }

}