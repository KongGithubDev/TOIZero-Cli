// C++ solution for A1-001
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string fname, lname;
    cin >> fname >> lname;
    
    cout << "Hello " << fname << " " << lname << endl;
    cout << fname.substr(0, 2) << lname.substr(0, 2) << endl;
    
    return 0;
}
