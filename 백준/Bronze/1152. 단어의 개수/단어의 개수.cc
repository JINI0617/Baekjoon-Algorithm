#include <iostream>
#include <string>
using namespace std;

//GPT 참고함..ㅜ

int main() {
    string input;
    getline(cin, input);  // 한 줄 전체 입력

    int count = 0;

    // 입력이 공백 한 줄만 들어오는 경우 예외 처리
    if (input != " ") {
        for (int i = 0; i < input.length(); i++) {
            // 공백 이전이 문자일 때 단어로 인식
            if (input[i] != ' ' && (i == 0 || input[i - 1] == ' ')) {
                count++;
            }
        }
    }

    cout << count << '\n';

    return 0;
}
