#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int n;cin>>n;
    int num;
    
    int *get = new int[n];
    for(int i =0; i<n; i++){
        cin>>num;
        get[i] = num;
    }
    
    sort(get, get+n);
    
    int m;cin>>m;
    int *card = new int[m];
    int *result_arr = new int[m];

    for(int i =0; i<m ;i++){
        cin>>num;
        card[i] = num;
        
        auto lower = lower_bound(get, get+n, num);
        auto upper = upper_bound(get, get+n, num);
        result_arr[i] = upper-lower;
    }
    
    
    
    for(int i =0; i< m; i++){
        cout<<result_arr[i]<<" ";
    }
    cout<<'\n';
    
    delete[] get;
    delete[] card;
    return 0;
}
