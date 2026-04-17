// C++ solution for A1-010
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n; char s;
    cin >> n >> s;
    if(s == 's' || s == 'S' || n < 18) printf("20");
    else printf("50");
    return 0;
}
