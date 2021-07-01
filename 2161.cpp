#include<iostream>
#include<queue>
using namespace std;

int main(){
    queue<int> que;
    int num;cin>>num;
    
    for(int i=1; i<=7; i++){
        que.push(i);
    }
    
    while(!que.empty()){
        cout<<que.front()<<" ";
        que.pop();
        que.push(que.front());
        que.pop
    }
    
    return 0;
}
