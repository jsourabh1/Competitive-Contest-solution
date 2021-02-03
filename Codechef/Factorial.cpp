
#include <iostream>
#define ll long long int
using namespace std;


int main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;i++){
        ll n,p,count=0;
        cin>>n;
        while(n!=0){
            n=n/5;//12
            count=count+n;
            if(n>5){
            n=n/5;
            count=count+n;
            }
        }
        cout<<count<<endl;
    }
	return 0;
	
}
