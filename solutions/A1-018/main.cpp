// C++ solution for A1-018
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    if(n < 0) {
        printf("Error : Please input positive number");
    }
    else if(n <= 0 || n > 9) {
        printf("Error : Out of range");
    } else {
        switch(n) {
            case 1: {
                cout << "I";
                break;
            }
            case 2: {
                cout << "II";
                break;
            }
            case 3: {
                cout << "III";
                break;
            }
            case 4: {
                cout << "IV";
                break;
            }
            case 5: {
                cout << "V";
                break;
            }
            case 6: {
                cout << "VI";
                break;
            }
            case 7: {
                cout << "VII";
                break;
            }
            case 8: {
                cout << "VIII";
                break;
            }
            case 9: {
                cout << "IX";
                break;
            }
            default: {
                cout << "Error";
                break;
            }
        }
    }
    return 0;
}
