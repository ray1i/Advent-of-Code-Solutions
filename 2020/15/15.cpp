//brute force sol'n, idc

#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main(){
    ifstream input;
    input.open("15.txt");

    string a;
    map<int, int> seen;

    int t = 1;
    while (getline(input, a, ',')){
        seen[stoi(a)] = t;
        t++;
    }

//part one:
    long long int cur;
    long long int next = 0;
    for (t; t<=2020; t++){
        cur = next;
        if (seen.count(cur) == 1){
            next = t - seen[cur];
        } else{
            next = 0;            
        }
        seen[cur] = t;
    }

    cout << "part one: " << cur << endl;

//part two:

    for (t; t<=30000000; t++){
        cur = next;
        if (seen.count(cur) == 1){
            next = t - seen[cur];
        } else{
            next = 0;            
        }
        seen[cur] = t;
    }

    cout << "part two: " << cur << endl;

    return 0;
}