// C++ solution for A1-036
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;

    n = (n / 10) * 10;

    for(int i = n; i >= 0; i -= 10) {
        cout << i << " ";
    }
    return 0;
}
