// C++ solution for A1-043
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int base, bonus, day;
    cin >> base >> bonus >> day;

    int total = base + bonus;

    if(day > 3) {
        total *= 1.5;
    }

    int rank;

    if(total >= 1500)
        rank = 5;
    else if(total >= 1000)
        rank = 4;
    else if(total >= 500)
        rank = 3;
    else if(total >= 200)
        rank = 2;
    else
        rank = 1;

    int special = 0;

    if(rank == 5 && day >= 7)
        special = 99;
    else if(rank == 4 && bonus > 300)
        special = 88;

    cout << total << '\n'
         << rank << '\n'
         << special;

    return 0;
}