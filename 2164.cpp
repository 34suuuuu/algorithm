#include<iostream>
#include<queue>
using namespace std;

int main() {
    queue<int> arr;
    int n; cin >> n;
    for (int i = 1; i <= n; i++) {
        arr.push(i);
    }

    while (arr.size() != 0) {
        if (arr.size() == 1)
            break;
        arr.pop();
        int temp = arr.front();
        arr.pop();
        arr.push(temp);
    }
    cout << arr.front() << '\n';
    return 0;
}
