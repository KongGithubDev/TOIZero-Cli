// C++ solution for A1-006
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n[2];
    cin >> n[0] >> n[1];
    if(n[0] % n[1] == 0) printf("yes");
    else printf("no");
    return 0;
}
