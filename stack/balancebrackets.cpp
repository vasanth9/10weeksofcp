/*A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {},and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given n strings of brackets, determine whether each sequence of 
brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.


INPUT:

The first line contains a single integer n, the number of strings. 

Each of the next n lines contains a single string s, a sequence of brackets.

CONSTRAINTS:

1<=n<=10^3
1<=|s|<=10^3, where  is the length of the sequence.
All chracters in the sequences ? { {, }, (, ), [, ] }.

OUTPUT:

For each string, return YES or NO.*/


//link:https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/balanced-brackets-3-4fc590c6/
 #include<bits/stdc++.h>
 using namespace std;
 int main()
 {
     //freopen("input.txt", "r", stdin); 
  
    // Printing the Output to output.txt file 
    //freopen("output.txt", "w", stdout); 
     int n;
     cin>>n;
     
     string s;
     while(n--){
         stack<char>brackets;
         cin>>s;
         int l=s.length();
         string ans="YES";
         for(int i=0;i<l;i++)
         {
             if(s[i]=='('||s[i]=='['||s[i]=='{')
             {
                 brackets.push(s[i]);
             }
             else if(s[i]==')')
             {   if(brackets.empty())
             {
                ans="NO"; break; 
             }
                 if(brackets.top()=='(')brackets.pop();
                 else {ans="NO"; break;}
             }
              else if(s[i]=='}')
             {if(brackets.empty())
             {
                ans="NO"; break; 
             }
                 if(brackets.top()=='{')brackets.pop();
                 else {ans="NO";break;}
             }
              else if(s[i]==']')
             {if(brackets.empty())
             {
                ans="NO"; break; 
             }
                 if(brackets.top()=='[')brackets.pop();
                 else {ans="NO";break;}
             }
             else{}
             

         }

         if(ans=="NO")
         cout<<ans<<"\n";
         else if(brackets.empty())cout<<"YES"<<"\n";
         else cout<<"NO\n";
        // cout<<brackets.size();
        //  while(!brackets.empty())
        //  {
        //      brackets.pop();
        //  }
     }
 }