#include <bits/stdc++.h>
using namespace std;

int countFreq(int arr[], int n) 
{ 
    unordered_map<int, int> mp; 
    for (int i = 0; i < n; i++) 
        mp[arr[i]]++; 
    int max = 0;
    for (auto x : mp) 
        if(x.second > max)
            max = x.second;
    return max;
} 

int main()
{
    int t;    cin>>t;
    while(t--){
        int n;   cin>>n;
        int arr[n];
        for(int i=0; i<n; i++)    cin>>arr[i];
        int ans = countFreq(arr,n);
        cout << ans << "\n";
    }
    return 0;
}
