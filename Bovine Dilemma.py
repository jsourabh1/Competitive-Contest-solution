#include <bits/stdc++.h>
#define ll long long int
using namespace std;
 
 
int main()
{
    ll t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin >> n;
        ll arr[n];
        for(ll i=0; i<n; i++)
        {
            cin >> arr[i];
        }
 
        float area = 0;
        set<float>s;
        for(ll i=0; i<n; i++)
        {
            for(ll j=i+1; j<n; j++)
            {
                area = (arr[j] - arr[i])/2.0;
                s.insert(area);
            }
        }
        
        cout << s.size() << "\n";
    }
    return 0;
}
