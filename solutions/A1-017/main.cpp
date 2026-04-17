// C++ solution for A1-017
#include <bits/stdc++.h>
#include <iomanip>
#include <sstream>
#include <ctime>
using namespace std;

time_t dateToTimestamp(int day, int month, int year) {
    tm tm = {};
    tm.tm_mday = day;
    tm.tm_mon = month - 1;  // tm_mon is 0-11
    tm.tm_year = year - 1900;  // tm_year is years since 1900
    tm.tm_hour = 0;
    tm.tm_min = 0;
    tm.tm_sec = 0;
    return mktime(&tm);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int day[2], month[2], year[2];
    cin >> year[0] >> month[0] >> day[0] >> year[1] >> month[1] >> day[1];
    
    time_t timestamp[2]; 
    timestamp[0] = dateToTimestamp(day[0], month[0], year[0]);
    timestamp[1] = dateToTimestamp(day[1], month[1], year[1]);

    if(timestamp[0] == timestamp[1]) printf("0");
    else if(timestamp[0] < timestamp[1]) printf("1");
    else printf("2");

    return 0;
}