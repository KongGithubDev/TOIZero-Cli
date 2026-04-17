// C++ solution for A1-011
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string n; int count = 1; char c;
    cin >> n;
    for (int i = 0; i < n.length(); i++) {
        if(i + 1 < n.length()) {
            if(n[i] == n[i + 1]) {
                count++;
            } else {
                printf("%d%c", count, n[i]);
                count = 1;
            }
        } else {
            printf("%d%c", count, n[i]);
        }
    }
    return 0;
}
