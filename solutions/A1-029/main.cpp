// C++ solution for A1-029
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string input; int result = 0;
    cin >> input;
    for(char &c : input) {
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') result++;
    }
    cout << result;
    return 0;
}
