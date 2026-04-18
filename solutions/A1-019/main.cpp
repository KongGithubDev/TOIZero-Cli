// C++ solution for A1-019
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n[3];
    cin >> n[0] >> n[1] >> n[2];
    if(n[0] == n[1] && n[1] == n[2]) {
        cout << "all the same";
    } else if(n[0] == n[1] || n[1] == n[2] || n[0] == n[2]) {
        cout << "neither";
    } else {
        cout << "all different";
    }
    return 0;
}
