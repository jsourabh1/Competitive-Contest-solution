#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;   cin>>t;
        while(t--){
            int n; cin>>n;
            int arr[n]; int e=0,o=0;
            for(int i=0; i<n; i++){
                cin>>arr[i];
                if(arr[i]%2 == 0)  e++;
            }
            o = n - e;
            int ans = min(o,e);
            cout << ans << "\n";
        }
    return 0;
}
