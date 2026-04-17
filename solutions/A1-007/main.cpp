// C++ solution for A1-007
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    char c;
    cin >> c;
    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
        printf("yes");
    } else {
        printf("no");
    }
    return 0;
}
