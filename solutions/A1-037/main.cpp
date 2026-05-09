// C++ solution for A1-037
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<pair<int, string>> roman = {
        {1000, "M"},
        {900, "CM"},
        {500, "D"},
        {400, "CD"},
        {100, "C"},
        {90, "XC"},
        {50, "L"},
        {40, "XL"},
        {10, "X"},
        {9, "IX"},
        {5, "V"},
        {4, "IV"},
        {1, "I"}
    };

    for(auto [value, symbol] : roman) {
        while(n >= value) {
            cout << symbol;
            n -= value;
        }
    }

    return 0;
}