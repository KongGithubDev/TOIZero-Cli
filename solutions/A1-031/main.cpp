// C++ solution for A1-031
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    string ans;
    int cnt = 0;

    for(int i = s.size() - 1; i >= 0; i--) {
        ans += s[i];
        cnt++;

        if(cnt % 3 == 0 && i != 0) {
            ans += ',';
        }
    }

    reverse(ans.begin(), ans.end());
    cout << ans;
    return 0;
}