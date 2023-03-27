// contest_id = "1809"
// problem_id = 'B'

#include <bits/stdc++.h>
using namespace std;
#define ll long long


void solve(){
    ll n; cin>>n;
    ll res = sqrt(n);
    while(1LL*res*res > n)
        res--;
    
    while(1LL*res*res < n)
        res++;
    
    cout<<res-1<<endl;
}

signed main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int test = 1;
  cin>>test;
  while (test--)
  {
    solve();
  }
  return 0; 
}

// this is my conmment0.4497493246870592
// this is my conmment0.680422465951087
// this is my conmment0.2258965106567581