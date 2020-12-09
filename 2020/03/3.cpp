#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main(){
    ifstream input;
    input.open("3.txt");

    vector<string> map;
    string a;

    if (input.is_open()){
        while (getline(input, a)){
            map.push_back(a);
        }
    } else cout << "file broke";
    input.close();
    
    char tree = '#';

    /* part one:
    vector<int> slope = {3, 1}; //right, down
    vector<int> cur = {0, 0}; // x, y

    int count = 0;
    while(cur[1] < map.size()){
        if (map[cur[1]][cur[0]] == tree) count++;
        
        cur[1] += slope[1];

        cur[0] += slope[0];
            if (cur[0] > map[cur[1]].size() - 1) cur[0] %= map[cur[1]].size();
    }
    cout << count; */

//part two:
    int slope[][2] = {{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}}; //right, down

    int count = 0;
    long long int prod = 1;
    for (int i = 0; i< sizeof(slope)/sizeof(slope[0]);i++){
        vector<int> cur = {0, 0}; // x, y
        while(cur[1] < map.size()){
            if (map[cur[1]][cur[0]] == tree) count++;
            
            cur[1] += slope[i][1];

            cur[0] += slope[i][0];
                if (cur[0] > map[cur[1]].size() - 1) cur[0] %= map[cur[1]].size();
        }
        prod *= count;
        count = 0;
    }

    cout << prod;

    return 0;
}