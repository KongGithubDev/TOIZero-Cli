// C++ solution for A1-051
#include <bits/stdc++.h>
using namespace std;

string caesarEncode(string text, int shift) {
    string result = "";
    shift = shift % 26;

    for (char &c : text) {
        if (isupper(c)) {
            result += char(int(c + shift - 'A') % 26 + 'A');
        } else if (islower(c)) {
            result += char(int(c + shift - 'a') % 26 + 'a');
        } else {
            result += c;
        }
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string in; int k;
    cin >> in >> k;
    if(k < 1 || k > 1000) return 0;
    cout << caesarEncode(in, k);
    return 0;
}
