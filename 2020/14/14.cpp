#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <bitset>
#include <regex>
//#include <math.h>

using namespace std;

long long int pow(int base, int power){
    long long int r = 1;
    for (int i = 0; i<power; i++){
        r *= base;
    }
    return r;
}

int main(){
//part one:
    ifstream input;
    input.open("14.txt");

    map<long long int, long long int> mem;
    map<int, int> mask;
    string cur;

    smatch address;

    while (getline(input, cur)){
        if (regex_search(cur, address, regex("mem\\[(\\d+)\\] = (\\d+)"))){
            bitset<36> temp = stoi(address[2]);
            for (auto const& x: mask){
                temp.set(35 - x.first, x.second);
            }
            mem[stoi(address[1])] = temp.to_ullong();            
        } else{
            mask.clear();
            for (int i = cur.find('=') + 2; i < cur.size(); i++){
                if (cur[i] != 'X') mask[i - cur.find('=') - 2] = static_cast<int>(cur[i]) - 48;
            }
        }
    }
    input.close();

    long long int sum = 0;
    for (auto const& x: mem) sum += x.second;

    cout << "part one: " << sum << endl;

//part two:

    input.open("14.txt");

    mem.clear();
    mask.clear();
    vector<long long int> floating;
    
    while (getline(input, cur)){
        if (regex_search(cur, address, regex("mem\\[(\\d+)\\] = (\\d+)"))){
            bitset<36> temp = stoi(address[1]);
            for (auto const& x: mask){
                temp.set(35 - x.first, x.second);
            }
            unsigned long long int base = temp.to_ullong();
            for (int i = 0; i<floating.size(); i++){
                mem[base + floating[i]] = stoi(address[2]);
            }
        } else{
            mask.clear();
            floating.clear();

            int it = cur.find('=') + 2;
            for (int i = it; i < cur.size(); i++){
                if (cur[i] == 'X') {
                    if (floating.empty()) {
                        floating.push_back(0);
                        floating.push_back(pow(2, 35-(i-it)));
                    } else{
                        vector<long long int> temp;
                        for (int j = 0; j<floating.size(); j++){
                            temp.push_back(floating[j] + pow(2, 35-(i-it)));
                        }
                        floating.insert(floating.begin(), temp.begin(), temp.end());
                    }
                    mask[i - it] = 0;
                } else if (cur[i] == '1') {
                    mask[i - it] = 1;
                }
            }
        }
    }
    input.close();

    sum = 0;
    for (auto const& x: mem) sum += x.second;

    cout << "part two: " << sum << endl;
    
    return 0;
}