#include<iostream>
#include<algorithm>
using namespace std;

void star(int x, int y, int num){
    if((x/num)%3 == 1 && (y/num)%3 == 1)
        cout<<" ";
    else
    {
        if(num / 3 == 0)
            cout<<"*";
        else
            star(x,y,num/3);
    }
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
  
    int n;cin>>n;
    
    for(int i =0; i< n; i++){
        for(int j =0; j< n; j++)
            star(i,j,n);
        cout<<'\n';
    }
    return 0;
}
