// C++ solution for A1-027
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string input;
    cin >> input;
    for (char &c : input) {
        c = std::tolower((unsigned char)c);
    }
    reverse(input.begin(), input.end());
    cout << input;
    return 0;
}
