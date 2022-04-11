#include<iostream>
#include<iomanip>
using namespace std;

int main(){
    int n,f;
    cin>>n;
    cin>>f;
    
    n=n/100*100;
    
    for(int i =0; i<100; i++){
        if((n+i)%f ==0){
            n+=i;
            break;
        }
            
    }
    cout<<n/10%10<<n%10<<'\n';
    return 0;
}
