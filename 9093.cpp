#include<iostream>
#include<stack>
#include<string>
#include<vector>

using namespace std;
int main() {
    int n;
    cin >> n;
    cin.ignore();
    
    while (n--) {
        string str;
        getline(cin, str);
        str += '\n';
        stack<char>s;
        
        for (char ch : str) {
            if (ch == '\n' || ch == ' ') {
                while (!s.empty()) {
                    cout << s.top();
                    s.pop();
                }
                cout << ch;
            }
            else {
                s.push(ch);
            }
        }
    }
    return 0;
}
