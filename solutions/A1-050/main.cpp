// C++ solution for A1-050
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    int male = 0;
    int female = 0;

    while(cin >> n) {
        if(n < 0)
            break;

        if(n % 2 == 0)
            female++;
        else
            male++;
    }

    cout << male << '\n' << female << '\n' << male + female;
    return 0;
}