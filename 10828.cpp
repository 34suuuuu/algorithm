#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main(){
    int n;
    string str;
    int m;
    stack<int>s;
    cin >> n;
    while (n--) {
        cin >> str;
        if (str == "push") {
            cin >> m;
            s.push(m);
        }
        else if (str == "pop") {
            if (s.size() == 0)
                cout << -1 << '\n';
            else {
                cout << s.top() << '\n';
                s.pop();
            }
        }
        else if (str == "size")
            cout << s.size() << '\n';
        else if (str == "empty")
            cout << s.empty() << '\n';
        else {
            if (s.size() == 0)
                cout << -1 << '\n';
            else
                cout << s.top() << '\n';
        }
    }
    return 0;
}
