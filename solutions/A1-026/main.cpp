// C++ solution for A1-026
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int result[2] = {0, 0};
    for(int i = 0; i < 3; i++) {
        int n;
        cin >> n;

        if(n % 2 == 0) result[0] ++;
        else result[1] ++;
    }

    cout << "even " << result[0] << "\nodd " << result[1];
    return 0;
}
