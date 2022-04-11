#include<iostream>
#include<stack>
using namespace std;

int main(){
    stack<int> st;
    int n;cin>>n;

    int num;
    while(n--){
        cin>>num;
        if(num == 0)
            st.pop();
        else
            st.push(num);

    }

    int sum=0;
    if(st.size() == 0) sum=0;
    else{
        while(!st.empty()){
            sum+=st.top();
            st.pop();
        }
    }
    cout<<sum<<'\n';

    return 0;
}
