// C++ solution for A1-044
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int age;
    string day;

    cin >> age >> day;

    int price;

    if(age < 5)
        price = 0;
    else if(age <= 18)
        price = 100;
    else
        price = 150;

    if(day == "Wed")
        price /= 2;

    cout << price;

    return 0;
}