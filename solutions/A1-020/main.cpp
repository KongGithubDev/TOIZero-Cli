// C++ solution for A1-020
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n[3];
    cin >> n[0] >> n[1] >> n[2];
    if(n[0] > n[1] && n[1] > n[2]) cout << "decreasing";
    else if(n[0] < n[1] && n[1] < n[2]) cout << "increasing";
    else cout << "neither";
    return 0;
}
