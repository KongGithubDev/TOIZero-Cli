// C++ solution for A1-015
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s; string stwo; int old;
    cin >> s >> stwo >> old;
    if(s.length() > 5) {
        string year = to_string(old);
        cout << s.substr(0, 2) << stwo.back() << year.back() << "\n";
    } else {
        cout << s.front() << old << stwo.back() << "\n";
    }
    return 0;
}
