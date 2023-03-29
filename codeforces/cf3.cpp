// contest_id = "1809"
// problem_id = 'A'

#include <bits/stdc++.h>
using namespace std;
#define ll long long


void solve(){
    string s; cin>>s;
    int maxEqual = 0;
    for(int i = 0; i<s.size(); i++){
        int curr = 1;
        for(int j = 0; j<s.size(); j++){
            if(i != j && s[i] == s[j]){
                curr++;
            }
            maxEqual = max(curr, maxEqual);
        }
    }
    if (maxEqual == 4){
        cout<<-1<<endl;
    }
    else if(maxEqual == 3){
        cout<<6<<endl;
    }
    else{
        cout<<4<<endl;
    }
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

// this is my conmment0.5736388611556043
// this is my conmment0.07666390850909488
// this is my conmment0.8933795888660773
// this is my conmment0.29925408517293695
// this is my conmment0.6707604580756169
// this is my conmment0.1434650161877229