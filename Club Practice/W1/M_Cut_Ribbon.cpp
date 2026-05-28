#include <bits/stdc++.h>
using namespace std;

int n, a, b, c;
vector<int> cuts;
map<int, int> dp;

int explore(int rem) {
    if (rem == 0) return 0; 
    if (rem < 0) return INT_MIN / 2;
    
    if (dp.find(rem) != dp.end()) {
        return dp[rem];
    }
    
    int res = INT_MIN / 2;
    for (int k : cuts) {
        res = max(explore(rem - k) + 1, res);
    }
    
    dp[rem] = res;
    return res;
}

int main() {
    cin >> n >> a >> b >> c;
    cuts = {a, b, c};
    sort(cuts.begin(), cuts.end());
    
    cout << explore(n) << endl;
    return 0;
}
