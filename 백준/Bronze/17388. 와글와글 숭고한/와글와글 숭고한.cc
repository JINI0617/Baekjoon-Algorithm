#include <iostream>
using namespace std;

int main() {
    
    int S, K, H;
    cin >> S >> K >> H;

    int total = S + K + H;

    if (total >= 100) 
        cout << "OK" << '\n';
    
    
    else {
        if (S < K && S < H) 
            cout << "Soongsil" << '\n';
        else if (K < S && K < H) 
            cout << "Korea" << '\n';
        else 
            cout << "Hanyang" << '\n';
    }

    return 0;
}
