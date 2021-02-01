#include <bits/stdc++.h>
#define int long long 
using namespace std;

signed main()
{
    int t;   cin>>t;
    while(t--){
        int n,k;  cin>>n>>k;
        int arr[n];
        int no_of_minus_one = 0, no_of_one = 0, no_of_zero = 0, no_of_excess_time = 0, others = 0;
        for(int i=0; i<n; i++){
            cin>>arr[i];
            if(arr[i] == 0)   no_of_zero++;
            else if(arr[i] == 1)   no_of_one++;
            else if(arr[i] == -1)   no_of_minus_one++;
            else if(arr[i] > k)  no_of_excess_time++;
            else others++;
        }
        int ans = n-no_of_minus_one;
        int c = ceil((float)n/2);
        if(ans < c)  cout << "Rejected" << "\n";
        else if(no_of_excess_time != 0) cout <<"Too Slow" << "\n";
        else if(no_of_one+no_of_zero == n)  cout << "Bot" << "\n";
        else cout << "Accepted" << "\n";
    }
}
