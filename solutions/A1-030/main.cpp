// C++ solution for A1-030
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    int input[n * 2], result = 0;
    for(int i = 1; i < n * 2; i+= 2) {
        if(i != 1) cout << " + ";
        cin >> input[i - 1] >> input[i];
        
        if(input[i - 1] >= input[i]) {
            cout << input[i - 1];
            result += input[i - 1];
        } else {
            cout << input[i];
            result += input[i];
        }
    }
    if(n != 1) cout << " = " << result;
    return 0;
}
