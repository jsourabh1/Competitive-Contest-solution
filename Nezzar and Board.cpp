#include<bits/stdc++.h>
#define ll long long
using namespace std; 
const ll maxn=200009;

 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    ll t;
    ll n,k;
    ll arr[maxn];
    cin>>t;
    while (t--){
        cin>>n>>k;
        for (ll i=0;i<n;++i) cin>>arr[i];
        sort(arr,arr+n);
        ll g=0;
        for (ll i=1;i<n;++i){
            g=__gcd(g,arr[i]-arr[0]);
        }
        if ((k-arr[0])%g) cout<<"NO\n";
        else cout<<"YES\n";
    }
    return 0;
}
