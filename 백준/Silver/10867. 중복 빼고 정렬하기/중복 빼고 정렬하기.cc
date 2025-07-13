#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> v(N);
    for (int i = 0; i < N; ++i) {
        cin >> v[i];
    }

    sort(v.begin(), v.end());


    cout << v[0] << " ";  
    for (int i = 1; i < N; ++i) {
        if (v[i] != v[i - 1]) {
            cout << v[i] << " ";
        }
    }

    return 0;
}
