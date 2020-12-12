#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main(){
    ifstream input;
    input.open("12.txt");

    vector<char> inst_chars;
    vector<int> inst_ints;
    string a;

    while (getline(input, a)) {
        inst_chars.push_back(a[0]);
        inst_ints.push_back(stoi(a.substr(1, 100)));
    }

    input.close();

//part one:
    int x = 0;
    int y = 0;
    map<int, vector<int>> dirs = {{0, {0, 1}},
                                {90, {1, 0}},
                                {180, {0, -1}},
                                {270, {-1, 0}}}; //rise, run
    int dir = 0;

    for (int i = 0; i<inst_chars.size(); i++){
        switch(inst_chars[i]){
            case 'N': 
                y += inst_ints[i];
                break;
            case 'S':
                y -= inst_ints[i];
                break;
            case 'E':
                x += inst_ints[i];
                break;
            case 'W': 
                x -= inst_ints[i];
                break;
            case 'L':
                dir += inst_ints[i];
                dir %= 360;
                break;
            case 'R':
                dir += 360 - inst_ints[i];
                dir %= 360;
                break;
            case 'F':
                x += inst_ints[i]*dirs[dir][1];
                y += inst_ints[i]*dirs[dir][0];
                break;
        }
    }

    cout << "part one: " << abs(x) + abs(y) << endl;

//part two:
    x = 0;
    y = 0;
    int slope[2] = {1, 10}; //rise, run

    for (int i = 0; i<inst_chars.size(); i++){
        switch(inst_chars[i]){
            case 'N': 
                slope[0] += inst_ints[i];
                break;
            case 'S':
                slope[0] -= inst_ints[i];
                break;
            case 'E':
                slope[1] += inst_ints[i];
                break;
            case 'W': 
                slope[1] -= inst_ints[i];
                break;
            case 'L':{
                if (inst_ints[i] == 90){
                    int temp = slope[1];
                    slope[1] = -slope[0];
                    slope[0] = temp;
                } else if (inst_ints[i] == 180){
                    slope[0] = -slope[0];
                    slope[1] = -slope[1];
                } else if (inst_ints[i] == 270){
                    int temp = slope[1];
                    slope[1] = slope[0];
                    slope[0] = -temp;
                }
            }
                break;
            case 'R':{
                if (inst_ints[i] == 90){
                    int temp = slope[1];
                    slope[1] = slope[0];
                    slope[0] = -temp;
                } else if (inst_ints[i] == 180){
                    slope[0] = -slope[0];
                    slope[1] = -slope[1];
                } else if (inst_ints[i] == 270){
                    int temp = slope[1];
                    slope[1] = -slope[0];
                    slope[0] = temp;
                }
            }
                break;
            case 'F':
                x += inst_ints[i]*slope[1];
                y += inst_ints[i]*slope[0];
                break;
        }
    }

    cout << "part two: " << abs(x) + abs(y) << endl;

    return 0;
}