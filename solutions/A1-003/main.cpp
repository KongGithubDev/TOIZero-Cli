// C++ solution for A1-003
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n[3] = {};
    for (int i = 0; i < 3; i++) {
        cin >> n[i];
    }
    printf("%d", max({n[0], n[1], n[2]}));
    return 0;
}
