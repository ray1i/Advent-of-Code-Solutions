#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main(){

    ifstream input;
    input.open("2.txt");

    vector<string> passwords;
    string a;

    while (getline(input, a)){
        passwords.push_back(a);
    }
    
    input.close();
    int total = 0;
    for (int i=0; i<passwords.size(); i++){
        int dash_pos = passwords[i].find("-");
        int space_pos = passwords[i].find(" ");

        char bad = passwords[i][space_pos + 1];

        int min = stoi(passwords[i].substr(0, dash_pos));
        int max = stoi(passwords[i].substr(dash_pos + 1, space_pos - 1 - dash_pos));

        string p = passwords[i].substr(space_pos + 4);

        /* part one
        int count = 0;
        for (int j=0; j<p.size(); j++){
            if (p[j] == bad) count++;
        }
        
        if (count >= min && count <= max) {
            total++;
        } */

        int count = 0;
        if (p[min - 1] == bad) count ++;
        if (p[max - 1] == bad) count ++;
        if (count == 1) total++;
    }
    
    cout << total;
    return 0;
}