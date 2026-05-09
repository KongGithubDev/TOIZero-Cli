// C++ solution for A1-040
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int total = 0;
    int n;

    while(true) {
        cin >> n;

        if(n == 5)
            break;

        if(n == 1)
            total += 100;
        else if(n == 2)
            total += 120;
        else if(n == 3)
            total += 200;
        else if(n == 4)
            total += 60;
    }

    cout << "Bye Bye\n";
    cout << "Total Calories: " << total;

    return 0;
}