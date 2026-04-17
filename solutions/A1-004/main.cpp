// C++ solution for A1-004
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n[3] = {}, scoremax[3] = { 10, 40, 50 };
    for (int i = 0; i < 3; i++) {
        cin >> n[i];
    }
    for (int i = 0; i < 3; i++) {
        double percent = (n[i] * 100) / scoremax[i];
        if(percent < 50.0) {
            printf("fail");
            return 0;
        }
    }
    printf("pass");
    return 0;
}
