#include <bits/stdc++.h>
#define int long long
using namespace std;

void solve()
{
    string str;   cin>>str;
    int n = str.length();
    int arr1[26] = {0};
    int arr2[26] = {0};
    int flag = 1;
    if(n%2 == 0)
    {
        for(int i=0; i<n/2; i++) { int c = str[i]; arr1[(c-97)]++;}
        for(int i=n/2; i<n; i++) { int p = str[i]; arr2[(p-97)]++;}

        for(int i=0; i<26; i++) {if(arr1[i] != arr2[i]) flag = 0;}
    }
    else
    {
        for(int i=0; i<n/2; i++) { int c = str[i]; arr1[(c-97)]++;}
        for(int i=n/2+1; i<n; i++) { int p = str[i]; arr2[(p-97)]++;}

        for(int i=0; i<26; i++) {if(arr1[i] != arr2[i]) flag = 0;}
    }
    if(flag == 1)  cout << "YES" << "\n";
    else cout << "NO" << "\n";
    
}

signed main()
{
    int t;    cin>>t;
    while(t--){
        solve();
    }
    return 0;
}
