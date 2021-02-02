
#include <iostream>
#define ll long long int
using namespace std;


int main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;i++){
        ll n,count=0,rem=0;
        cin>>n;
        while(n!=0){
        	rem=n%10;
        	count=count*10+rem;
        	n=n/10;
            }
        cout<<count<<endl;
    }
	return 0;
	
}
