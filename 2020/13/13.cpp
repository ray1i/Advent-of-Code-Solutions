#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main(){
    ifstream input;
    input.open("13.txt");

    int start;
    string a;
    getline(input, a);
    start = stoi(a);

    vector<int> ids;
    while (getline(input, a, ',')) {
        if (a != "x") ids.push_back(stoi(a));
        else ids.push_back(0);
    }

    input.close();

//part one:
    int mintime = 10000000;
    int minid;

    for (int i = 0; i<ids.size(); i++){
        if (ids[i] != 0 && start - (start%ids[i]) + ids[i] < mintime){
            mintime = start - (start%ids[i]) + ids[i];
            minid = ids[i];
        }
    }
    cout << "part one: " << (mintime - start) * minid << endl;

//part two:
    long long int m = ids[0]; //multiple of 1st id
    long long int it = ids[0];

    for (int i = 1; i<ids.size(); i++){
        if (ids[i] != 0){
            while ((m + i) % ids[i] != 0) m += it;
            it *= ids[i];
        }
    }

    cout << "part two: " << m << endl;

    return 0;
}