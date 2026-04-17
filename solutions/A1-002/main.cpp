// C++ solution for A1-002
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    vector<int> coins = {10, 5, 2, 1};
    int coinkeep = n;
    int keep[11] = {};
    
    for (int coin : coins) {
        while (coinkeep >= coin) {
            coinkeep -= coin;
            keep[coin] ++;
        }
        printf("%d = %d\n", coin, keep[coin]);
    }

    return 0;
}