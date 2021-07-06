#include<iostream>
#include<queue>
using namespace std;

int main(){
    int count=0;
    int num, index, imp;
    int test; cin>>test;
    
    for(int i =0; i<test; ++i){
        count =0;
        cin>>num>>index;
        queue<pair<int, int>> q;
        priority_queue<int>pq;
        
        for(int j =0; j<num; ++j){
            cin>>imp;
            q.push({j,imp});
            pq.push(imp);
        }
        
        while(!q.empty()){
            int first = q.front().first;
            int second = q.front().second;
            q.pop();
            
            if(pq.top() == second){
                pq.pop();
                ++count;
                if(first == index){
                    cout<<count<<'\n';
                    break;
                }
            }
            else q.push({first, second});
        }
    }
}
