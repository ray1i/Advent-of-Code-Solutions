#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <cmath>

using namespace std;

int main(){
    ifstream input;
    input.open("10.txt");

    vector<int> jolts = {0};
    string a;
    while (getline(input, a)) jolts.push_back(stoi(a));

    input.close();

//part one:
    sort(jolts.begin(), jolts.end());
    jolts.push_back(jolts[jolts.size() - 1] + 3);

    int one_count = 0;
    int three_count = 0;
    for (int i=1; i<jolts.size();i++){
        if (jolts[i] - jolts[i - 1] == 1) one_count++;
        else if (jolts[i] - jolts[i - 1] == 3) three_count++;
    }
    cout << "part one: " << one_count * three_count << endl;

//part two:
    //three in a row = 2 possibilities
    //four in a row = 4 possibilities
    //five in a row = 7 possibiltiies
    //six in a row = 11 possibilities
    //possibilities = the previous possiblities + chain - 2
    
    map<int, int> chains;
    int curchain = 1;
    for (int i=1; i<jolts.size();i++){
        if (jolts[i] - jolts[i - 1] == 1) {
            curchain++;
        }
        else if (jolts[i] - jolts[i - 1] == 3) {
            if (chains.count(curchain) == 0) chains[curchain] = 0;
            chains[curchain]++;
            curchain = 1;
        }
    }

    int curp = 1;
    long long int total = 1;
    for (int i = 3; i<=chains.size(); i++){
        curp += i - 2;
        if (chains.count(i) == 1) {
            total *= pow(curp, chains[i]);
        }
    }

    cout << "part two: " << total << endl;

    return 0;
}