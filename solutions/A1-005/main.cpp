// C++ solution for A1-004
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n[2] = {};
    for (int i = 0; i < 2; i++) {
        cin >> n[i];
    }

    vector<string> arr = { "winter", "spring", "summer", "fall" };
    if(n[1] >= 21) {
        n[0] = n[0] % 12 + 1;  // 12→1, 1→2, ...
    }

    int weather = (n[0] + 2) / 3;
    printf("%s", arr[weather - 1].c_str());
    return 0;
}
