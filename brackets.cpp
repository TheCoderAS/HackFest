#include <bits/stdc++.h>

using namespace std;

// Complete the isBalanced function below.
string isBalanced(string s) {
    int length=s.length();
    stack<char>st;
    if(length%2==0){
        for(int i=0;i<length;i++){
            if(s[i]=='('||s[i]=='{'||s[i]=='['){
                st.push(s[i]);
            }else{
                if(s[i]==')'&&s[i-1]=='(')
                    st.pop();
                else if(s[i]=='}'&&s[i-1]=='{')
                    st.pop();
                else if(s[i]==']'&&s[i-1]=='[')
                    st.pop();
                else
                    st.push(s[i]);
            }
        }
    }else{
        return "NO";
    }
    if(st.empty())
        return "YES";
    else
        return "NO";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string s;
        getline(cin, s);

        string result = isBalanced(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
