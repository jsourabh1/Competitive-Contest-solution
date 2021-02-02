#include<bits/stdc++.h>
using namespace std;
#define ll long long
void solve()
{
	ll t,laddu=0;
	string s;
	cin>>t>>s;
	for(ll i=0;i<t;i++)
	{
		string str;
		cin>>str;
		if(str=="CONTEST_WON")
		{
			ll rank,bonus=0;
			cin>>rank;
			if(rank<=20) 
            bonus=20-rank;
			laddu+=300+bonus;
		}
        else if(str=="TOP_CONTRIBUTOR"){
			laddu+=300;
		}
        else if(str=="BUG_FOUND"){
			ll sev;
			cin>>sev;
			laddu+=sev;
		}
        else if(str=="CONTEST_HOSTED") laddu+=50;}
	if(s=="INDIAN")
	{
		cout<<laddu/200<<endl;
	}else{
		cout<<laddu/400<<endl;
	}
}
int main()
{
	ll t;
	cin>>t;
	while(t--)
	{
		solve();
	}
    return 0;
}
