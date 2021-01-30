#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main()
{
    int t;
    cin>>t;
    while(t--)
    {

        int n,x;
        cin>>n>>x;
        int flag=false;
        for(int i=1;i<=n;i++){
            if(x%i==0 && x/i<=n) {flag=true; break;}
        }
        if(flag) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
    return 0;
}
