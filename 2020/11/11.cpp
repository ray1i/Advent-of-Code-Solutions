// slowest code in existence. it took me like 10 minutes to run and i'm too lazy to come up with a better algorithm

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int directions[8][2] = {
    {-1, 0},
    {-1, 1},
    {0, 1},
    {1, 1},
    {1, 0},
    {1, -1},
    {0, -1},
    {-1, -1}
};
//column, row
//top left is 0,0
//starts from north, clockwise

int surroundings(int row, int column, vector<vector<char>> layout){
    int count = 0;
    for (int dir = 0; dir<8; dir++){
        if (row + directions[dir][0] >= 0 &&
            row + directions[dir][0] < layout.size() &&
            column + directions[dir][1] >= 0 &&
            column + directions[dir][1] < layout[row].size()){
            if (layout[row + directions[dir][0]][column + directions[dir][1]] == '#') count++;
        }
    }
    return count;
}

int surroundings2(int row, int column, vector<vector<char>> layout){
    int count = 0;
    for (int dir = 0; dir<8; dir++){
        int m = 1;
        while (row + m*directions[dir][0] >= 0 &&
            row + m*directions[dir][0] < layout.size() &&
            column + m*directions[dir][1] >= 0 &&
            column + m*directions[dir][1] < layout[row].size()){
            if (layout[row + m*directions[dir][0]][column + m*directions[dir][1]] == '#'){
                count++;
                break;
            } else if (layout[row + m*directions[dir][0]][column + m*directions[dir][1]] == 'L'){
                break;
            }
            m++;
        }
    }
    return count;
}

void print_layout(vector<vector<char>> layout){
    for (int i = 0; i<layout.size(); i++){
        for (int j=0; j<layout[i].size(); j++){
            cout << layout[i][j] << " ";
        }
        cout << endl;
    }
}

int main(){
    ifstream input;
    input.open("11.txt");

    vector<vector<char>> _layout;
    string a;

    while (getline(input, a)) {
        vector<char> temp;
        for (int i=0; i<a.length(); i++) temp.push_back(a[i]);
        _layout.push_back(temp);
    }

    input.close();

//part one:
    vector<vector<char>> prev_layout;
    vector<vector<char>> layout = _layout;
    vector<vector<char>> next_layout = layout;
    int it = 0;
    while (prev_layout != layout){
        for (int i = 0; i<layout.size(); i++){
            for (int j=0; j<layout[i].size(); j++){
                if (layout[i][j] == 'L'){
                    if (surroundings(i, j, layout) == 0) {
                        next_layout[i][j] = '#';
                    }
                } else if (layout[i][j] == '#'){
                    if (surroundings(i, j, layout) >= 4) {
                        next_layout[i][j] = 'L';
                    }
                }
            }
        }
        prev_layout = layout;
        layout = next_layout;
        it++;
        cout << it << " ";
    }

    int occupied_count = 0;
    for (int i = 0; i<layout.size(); i++){
        for (int j=0; j<layout[i].size(); j++){
            if (layout[i][j] == '#') occupied_count++;
        }
    }

    cout << "part one: " << occupied_count << endl;

//part two:
    prev_layout.clear();
    layout = _layout;
    next_layout = layout;

    it = 0;
    while (prev_layout != layout){
        for (int i = 0; i<layout.size(); i++){
            for (int j=0; j<layout[i].size(); j++){
                if (layout[i][j] == 'L'){
                    if (surroundings2(i, j, layout) == 0) {
                        next_layout[i][j] = '#';
                    }
                } else if (layout[i][j] == '#'){
                    if (surroundings2(i, j, layout) >= 5) {
                        next_layout[i][j] = 'L';
                    }
                }
            }
        }
        prev_layout = layout;
        layout = next_layout;
        it++;
        cout << it << " ";
        //print_layout(layout);
        //cout << "------";
    }

    occupied_count = 0;
    for (int i = 0; i<layout.size(); i++){
        for (int j=0; j<layout[i].size(); j++){
            if (layout[i][j] == '#') occupied_count++;
        }
    }

    cout << "part two: " << occupied_count << endl;

    return 0;
}