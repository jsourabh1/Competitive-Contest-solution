#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main()
{
    int t;  cin>>t;
    while (t--)
    {
        int x,y,z;   cin>>x>>y>>z; int flag = 0;
        if(x == (y+z))  flag = 1;
        else if(y == (x+z))  flag = 1;
        else if(z == (x+y))  flag = 1;
        if(flag == 1) cout << "YES" << "\n";
        else cout << "NO" << "\n";
    }
    return 0;
}
