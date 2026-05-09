// C++ solution for A1-032
#include <bits/stdc++.h>
using namespace std;

string repeat(int n, string s) {
    if(n <= 0) return "";
    
    string r;
    while(n--) r += s;
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;

    cout << repeat(n, "*") << "\n" << repeat(n - 2, "*") << "\n" << repeat(n - 4, "*");
    return 0;
}