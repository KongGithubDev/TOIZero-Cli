// C++ solution for A1-012
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, original; char c;
    cin >> n >> c;
    if(n < 10 || n > 99) return 0; 

    original = n;

    string s = to_string(n);
    reverse(s.begin(), s.end());
    int rev = stoi(s);

    int sum;
    if(c == '+') {
        sum = original + rev;
    }
    else if(c == '*') {
        sum = original * rev;
    }
    printf("%d %c %d = %d", original, c, rev, sum);
    return 0;
}

int reverse(int n, int rev = 0) {
    return n == 0 ? rev : reverse(n / 10, rev * 10 + n % 10);
}