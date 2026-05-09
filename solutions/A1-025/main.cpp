#include <bits/stdc++.h>
using namespace std;

string getname(string input) {
    if(input == "A") return "ace";
    else if(input == "J") return "jack";
    else if(input == "Q") return "queen";
    else if(input == "K") return "king";

    else if(input == "D") return "diamonds";
    else if(input == "H") return "hearts";
    else if(input == "S") return "spades";
    else if(input == "C") return "clubs";

    return input;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string input;
    cin >> input;
    
    for(char &c : input) {
        c = toupper(c);
    }

    string last(1, input.back());
    string front = input.substr(0, input.size() - 1);

    cout << getname(front) << " of " << getname(last);

    return 0;
}