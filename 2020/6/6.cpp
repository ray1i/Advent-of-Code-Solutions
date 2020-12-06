#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main(){
    ifstream input;
    input.open("6.txt");

    vector<string> answers;
    string a;

    while (getline(input, a)) answers.push_back(a);

    input.close();

//part one:
    map<char, int> q = {};
    int total = 0;
    for (int i = 0; i < answers.size(); i++){
        if (answers[i] != "") for (int j = 0; j < answers[i].size(); j++) q[answers[i][j]] = 1;
        else {
            total += q.size();
            q.clear();
        }
    }
    total += q.size();

    cout << "part one " << total << endl;

//part two:
    q.clear();
    total = 0;
    int max = 0;
    for (int i = 0; i < answers.size(); i++){
        if (answers[i] != "") {
            for (int j = 0; j < answers[i].size(); j++) {
                if (q.count(answers[i][j]) == 1) q[answers[i][j]]++;
                else q[answers[i][j]] = 1;
            }
            max++;
        }
        else {
            for (auto const &p : q) if (q[p.first] == max) total++;
            q.clear();
            max = 0;
        }
    }
    for (auto const &p : q) if (q[p.first] == max) total++;

    cout << "part two " << total << endl;

    return 0;
}