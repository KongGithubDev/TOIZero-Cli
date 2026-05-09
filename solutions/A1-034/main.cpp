// C++ solution for A1-034
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int least;
    cin >> least;

    for(int i = 1; i < n; i++) {
        int in;
        cin >> in;

        if(least > in)
            least = in;
    }

    cout << least;

    return 0;
}