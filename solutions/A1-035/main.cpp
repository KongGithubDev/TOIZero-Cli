// C++ solution for A1-035
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;

    int result = 0;
    for(int i = 0; i < n; i++) {
        result += pow(i + 1, 2);
    }
    cout << result;
    return 0;
}
