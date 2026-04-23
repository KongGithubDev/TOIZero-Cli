// C++ solution for A1-023
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    char c;
    cin >> n >> c;
    c = toupper(c);
    if((c == 'F' && n > 32) || (c == 'C' && n == 0)) {
        cout << "solid";
    } else if((c == 'F' && n >= 212) || (c == 'C' && n >= 100)) {
        cout << "gas";
    } else if((c == 'F' && n >= 32) || (c == 'C' && n > 0)) {
        cout << "liquid";
    }
    return 0;
}
