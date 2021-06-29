#include<iostream>
#include<stack>
#include<string>
using namespace std;
int main() {
    stack<char>st;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        for (int j = 0; j < str.length(); j++) {
            if (str[j] == '(' || st.empty())
                st.push(str[j]);
            else if (st.top() == '(')
                st.pop();
        }
        if (st.empty())
            cout << "YES" << '\n';
        else
            cout << "NO" << '\n';
        while (!st.empty())
            st.pop();
    }
    return 0;
}

