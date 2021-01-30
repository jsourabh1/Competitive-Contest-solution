#include <bits/stdc++.h>
#define ll long long int
using namespace std;

ll solve()
{
    ll n; cin>>n;
    string str;  cin>>str;
    priority_queue<int> pq;
        ll ans = 0;
        for(int i=0; i<n; i++){
            ll curr = str[i] - '0';
            if(!pq.empty() && pq.top()>curr){
                ans+= pq.top() - curr;
                pq.pop();
                pq.push(curr);
            }
            pq.push(curr);
        }
        return ans;
}

int main()
{
    ll t;   cin>>t;
    while(t--){
        cout << solve() << "\n";
    }
    return 0;
}
