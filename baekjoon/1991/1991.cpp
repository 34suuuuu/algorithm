#include<iostream>
using namespace std;

int T[27][2];
void postorder(int node) {
    if (node== -1)return;
    postorder(T[node][0]);
    postorder(T[node][1]);
    cout << char(node + 'A');
}

void inorder(int node) {
    if (node == -1)return;
    inorder(T[node][0]);
    cout << char(node + 'A');
    inorder(T[node][1]);
}

void preorder(int node) {
    if (node == -1)return;
    cout << char(node + 'A');
    preorder(T[node][0]);
    preorder(T[node][1]);
    
}

int main() {
    int n;
    cin >> n;
    char x, y, z;
    while (n--) {
        cin >> x >> y >> z;
        x -= 'A';
        if (y == '.')
            T[x][0] = -1;
        else
            T[x][0] = y - 'A';
        if (z == '.')
            T[x][1] = -1;
        else
            T[x][1] = z - 'A';
    }
    preorder(0);
    cout << '\n';
    inorder(0);
    cout << '\n';
    postorder(0);
    cout << '\n';
    return 0;
}
