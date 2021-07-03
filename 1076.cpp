#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int output[3];

int main(){
    string color[10] = {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
    string input[3];
    
    for(int i =0; i< 3; i++){
        cin>>input[i];
    }
    
    for(int i =0; i<3; i++){
        for(int j =0; j< 10; j++){
            if(input[i] == color[j]){
                output[i] = j;
                break;
            }
                
        }
    }
    
    int result = output[0] * 10 + output[1];
   
    if(result == 0){
        cout<<"0"<<'\n';
        return 0;
    }
    else{
        cout<<result;
        for(int i =0; i< output[2]; i++){
            cout<<"0";
        }
        cout<<'\n';
    }
    
    return 0;
}
