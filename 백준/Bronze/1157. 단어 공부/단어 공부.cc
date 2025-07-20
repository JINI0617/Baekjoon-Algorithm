#include <iostream>
#include <map>
#include <string>
#include <cctype>
using namespace std;

int main(){
    
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int maxValue = 0;
    char maxKey;
    bool isDuplicated = false;
    
    string s;
    cin >> s;
    
    for(char& c: s)
        c = toupper(c);
    
    map<char, int> myWord;
    
    for(char c: s)
        myWord[c]++;
    
    for(const auto& entry: myWord)
    {
        if(entry.second > maxValue)
        {
            maxValue = entry.second;
            maxKey = entry.first;
            isDuplicated = false;
        }
        else if(entry.second == maxValue)
            isDuplicated = true;
    
    }
    
    if(isDuplicated)
        cout << "?";
    else
        cout << maxKey;
}
