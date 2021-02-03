#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main()
{
    int n; cin>>n;
    int arr[n];
    int m = 0;
    for(int i=0; i<n; i++)  cin>>arr[i];
    sort(arr,arr+n,greater<int>());
    for(int i=0; i<n; i++)
    {
        int ans = (i+1)*arr[i];
        m = max(ans,m);
    }
    cout << m << "\n";
    return 0;
}
