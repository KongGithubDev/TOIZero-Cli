// C++ solution for A1-049
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    while(s.size() < 5)
        s = "0" + s;

    int a = s[0] - '0';
    int b = s[1] - '0';
    int c = s[2] - '0';
    int d = s[3] - '0';
    int e = s[4] - '0';

    int floor = 13;
    if(a > 5) floor = 9;
    else if(b > 5) floor = 10;
    else if(c > 5) floor = 11;
    else if(d > 5) floor = 12;
    else if(e > 5) floor = 14;

    bool pal = (s == string(s.rbegin(), s.rend()));

    int r1 = 0;
    if(pal) {
        if(a + e > 5)
            r1 = 1;
        else if(b * d > 5)
            r1 = 2;
    }
    else {
        if(e != 0 && a / e > 5)
            r1 = 1;
        else if(b - e > 5)
            r1 = 2;
    }

    int r2 = 0;
    int sum = a + b + c + d + e;
    int mul = a * b * c * d * e;

    if(sum > 25)
        r2 = 1;
    else if(mul > 55)
        r2 = 2;

    cout << floor << r1 << r2;

    return 0;
}