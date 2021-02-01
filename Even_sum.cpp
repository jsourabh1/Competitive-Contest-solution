#include <bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
    ll t; cin>>t;
    while(t--){
        ll n;  cin>>n;
        ll arr[n]; 
        ll sum=0;
        for(int i=0; i<n; i++){
            cin>>arr[i];
            sum = sum + arr[i];
        }
        if(sum%2 == 0)  cout << "1" << "\n";
        else cout << "2" << "\n";
    }
    return 0;
}
