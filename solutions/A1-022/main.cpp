// C++ solution for A1-022
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int d, m;
    cin >> d >> m;
    
    string zodiac;
    if ((m == 12 && d >= 22) || (m == 1 && d <= 19)) zodiac = "capricorn";
    else if ((m == 1 && d >= 20) || (m == 2 && d <= 18)) zodiac = "aquarius";
    else if ((m == 2 && d >= 19) || (m == 3 && d <= 20)) zodiac = "pisces";
    else if ((m == 3 && d >= 21) || (m == 4 && d <= 19)) zodiac = "aries";
    else if ((m == 4 && d >= 20) || (m == 5 && d <= 20)) zodiac = "taurus";
    else if ((m == 5 && d >= 21) || (m == 6 && d <= 21)) zodiac = "gemini";
    else if ((m == 6 && d >= 22) || (m == 7 && d <= 22)) zodiac = "cancer";
    else if ((m == 7 && d >= 23) || (m == 8 && d <= 22)) zodiac = "leo";
    else if ((m == 8 && d >= 23) || (m == 9 && d <= 22)) zodiac = "virgo";
    else if ((m == 9 && d >= 23) || (m == 10 && d <= 23)) zodiac = "libra";
    else if ((m == 10 && d >= 24) || (m == 11 && d <= 21)) zodiac = "scorpio";
    else zodiac = "sagittarius";
    
    cout << zodiac << endl;
    
    return 0;
}
