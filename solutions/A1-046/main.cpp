// C++ solution for A1-046
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int sum = 0;
    int even = 0;
    int odd = 0;

    for(int i = 0; i < n; i++) {
        int x;
        cin >> x;

        sum += x;

        if(x % 2 == 0)
            even++;
        else
            odd++;
    }

    cout << "SUM " << sum << '\n';
    cout << "EVEN " << even << '\n';
    cout << "ODD " << odd;
    return 0;
}