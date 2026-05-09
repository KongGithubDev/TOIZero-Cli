// C++ solution for A1-024
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n[2]; cin >> n[0] >> n[1];
    int tax;
    if(n[0] >= 2000) {
        if(n[1] <= 1500) tax = 1000;
        else if(n[1] <= 2000) tax = 1200;
        else tax = 1500;
    } else if(n[0] >= 1991) {
        if(n[1] <= 1500) tax = 1100;
        else if(n[1] <= 2000) tax = 1300;
        else tax = 1700;
    } else {
        if(n[1] <= 1500) tax = 1250;
        else if(n[1] <= 2000) tax = 1400;
        else tax = 2000;
    }
    printf("%d", tax);
    return 0;
}
