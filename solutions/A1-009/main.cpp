// C++ solution for A1-009
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n[2], sum;
    cin >> n[0] >> n[1];
    sum = n[0] + n[1];
    printf("%d\n", sum);
    if(sum >= 50) printf("pass");
    else printf("fail");
    return 0;
}
