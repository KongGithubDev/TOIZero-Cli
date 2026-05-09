// C++ solution for A1-047
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, a;
    cin >> n >> a;

    int total = n * a;

    if(total == 0) {
        cout << "No teaching";
        return 0;
    }

    int hours = total / 60;
    int minutes = total % 60;

    if(hours > 0) {
        cout << hours << " hours";

        if(minutes > 0)
            cout << " ";
    }

    if(minutes > 0) {
        cout << minutes << " minutes";
    }
    return 0;
}