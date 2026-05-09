// C++ solution for A1-033
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    char input[n]; int result = 0;
    for(int i = 0; i < n; i++) {
        cin >> input[i];
        if(input[i] == 'A' || input[i] == 'E' || input[i] == 'I' || input[i] == 'O' || input[i] == 'U') result++;
    }
    cout << result;
    return 0;
}
