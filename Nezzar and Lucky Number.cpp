#include <bits/stdc++.h>
#define ll long long int
using namespace std;

ll solve(ll temp,int d){
    ll flag = 0;
    while(temp > 0){
        ll c = temp % 10;
        if(c == d)   flag = 1;
        temp = temp / 10;
   }
   return flag;
}

int main()
{
    ll t;   cin>>t;
    while(t--)
    {
        ll q,d;    cin>>q>>d;
        ll arr[q];
        for(ll i=0; i<q; i++)    cin>>arr[i];
        int flag = 0;
        for(ll i=0; i<q; i++)
        {
            if(arr[i]%d == 0)    cout << "YES" << "\n";
            else if(arr[i] >= 100)  cout << "YES" << "\n";
            else
            {
                flag = 0;
                while(arr[i] > 0)
                {
                    ll ans = solve(arr[i],d);
                    if(ans == 1) flag = 1;
                    arr[i] = arr[i] - d;
                }
                if(flag == 1)  cout << "YES" << "\n";
                else cout << "NO" << "\n";
                
            }
        }
    }
    return 0;
}
