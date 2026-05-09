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
    if(c == 'F') n = (n - 32) / 1.8;

    if(n <= 0) {
        cout << "solid";
    } else if(n >= 100) {
        cout << "gas";
    } else if(n > 0) {
        cout << "liquid";
    }
    return 0;
}