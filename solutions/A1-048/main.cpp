// C++ solution for A1-048
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int unit = n;
    double subtotal = 0;
    if(n > 200) {
        subtotal += (n - 200) * 15;
        n = 200;
    }

    if(n > 100) {
        subtotal += (n - 100) * 12;
        n = 100;
    }

    if(n > 50) {
        subtotal += (n - 50) * 10;
        n = 50;
    }

    if(n > 10) {
        subtotal += (n - 10) * 7;
        n = 10;
    }

    subtotal += n * 5;

    double ft = unit * 0.50;
    double vat = subtotal * 0.07;
    double total = subtotal + ft + vat;
    cout << fixed << setprecision(2) << total;
    return 0;
}