// C++ solution for A1-013
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    char c; string n;
    cin >> c >> n;

    char correct_c = 'H'; string correct_n = "4567";
    if(correct_c == c && correct_n == n) printf("safe unlocked");
    else if(correct_c != c && correct_n != n) printf("safe locked");
    else if(correct_c == c) printf("safe locked - change digit");
    else if(correct_n == n) printf("safe locked - change char");
    return 0;
}
