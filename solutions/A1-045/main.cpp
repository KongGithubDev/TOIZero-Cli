// C++ solution for A1-045
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int price = 35;

    if(n > 1) {
        if(n <= 10) {
            price += (n - 1) * 5;
        }
        else {
            price += 9 * 5;
            price += (n - 10) * 8;
        }
    }
    cout << price;
    return 0;
}