#include <bits/stdc++.h>
#define int int32_t
using namespace std;

signed main()
{
    cin.sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;  cin>>t;
    while(t--)
    {
        int n;  cin>>n;
        int arr[n];
        for(int i=0; i<n; i++)  cin>>arr[i];
        int m = arr[0];
        int ctr = 1;
        for(int i=1; i<n; i++)
        {
            m = min(m,arr[i]);
            if(arr[i] <= m) ctr++;
        }
        cout << ctr << "\n";
    }
    return 0;
}
