// C++ solution for A1-028
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    if(n < 1000 || n > 9999) return 0;

    string input = to_string(n);
    reverse(input.begin(), input.end());
    cout << input;
    return 0;
}
