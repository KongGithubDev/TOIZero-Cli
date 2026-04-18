// C++ solution for A1-021
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;

    bool isleapyear = false;
    if(n < 1582) {
        isleapyear = (n % 4 == 0);
    } else {
        if(n % 4 == 0) {
            if(n % 100 == 0) {
                isleapyear = (n % 400 == 0);
            } else {
                isleapyear = true;
            }
        } else {
            isleapyear = false;
        }
    }

    printf(isleapyear ? "yes" : "no");
    return 0;
}
