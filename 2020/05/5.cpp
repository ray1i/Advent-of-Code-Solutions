#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

int get_row(string s){
    float min = 0;
    float max = 127;
    
    for (int i = 0; i < 7; i++){
        if (s[i] == 'F') max = min + (max - min)/2;
        else if (s[i] == 'B') min = min + (max - min)/2;
    }
    if (ceil(min) == floor(max)) return ceil(min);
    else cout << min << " " << max << endl;
    return -1;
}

int get_column(string s){
    float min = 0;
    float max = 7;
    
    for (int i = 7; i < 10; i++){
        if (s[i] == 'L') max = min + (max - min)/2;
        else if (s[i] == 'R') min = min + (max - min)/2;
    }
    if (ceil(min) == floor(max)) return ceil(min);
    else cout << max << " " << min << endl;
    return -1;
}

int main(){
    ifstream input;
    input.open("5.txt");
    
    vector<string> seats;
    string a;
    while (getline(input, a)) seats.push_back(a);

    input.close();

// part one:
    int max_id = 0;
    int min_id = 1000;
    for (int i = 0; i < seats.size(); i++){
        if (get_row(seats[i]) * 8 + get_column(seats[i]) > max_id) max_id = get_row(seats[i]) * 8 + get_column(seats[i]);
        if (get_row(seats[i]) * 8 + get_column(seats[i]) < min_id) min_id = get_row(seats[i]) * 8 + get_column(seats[i]);
    }

    cout << "max_id : " << max_id << endl;

//part two:
    int ids[max_id] = {};
    for (int i = 0; i < seats.size(); i++){
        ids[get_row(seats[i]) * 8 + get_column(seats[i])] = 1;
    }

    for (int i = min_id; i < max_id; i++){
        if (ids[i] == 0){
            cout << "my id: " << i;
            break;
        }
    }
    
    return 0;
}