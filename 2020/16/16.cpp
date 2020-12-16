//i hate this solution.

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <regex>

using namespace std;

bool in_range(int num, vector<int> ranges){
    return ((num >= ranges[0] && num <= ranges[1]) || (num >= ranges[2] && num <= ranges[3]));
}

bool contains(vector<string> v, string s){
    if (find(v.begin(), v.end(), s) == v.end()) return false;
    else return true;
}

int main(){
    ifstream input;
    input.open("16.txt");

    string a;

    map<string, vector<int>> rules;
    smatch s;
    while (getline(input, a) && a != ""){
        if (regex_match(a, s, regex("(\\D+): (\\d+)-(\\d+) or (\\d+)-(\\d+)"))){
            for (int i = 2; i<=5; i++) rules[s[1]].push_back(stoi(s[i]));
        }
    }

    vector<int> my_ticket;
    while (getline(input, a) && a != ""){
        while (regex_search(a, s, regex("(\\d+)"))){
            my_ticket.push_back(stoi(s[0]));
            a = s.suffix().str();
        }
    }
    vector<vector<int>> tickets;
    while (getline(input, a)){
        vector<int> temp;
        while (regex_search(a, s, regex("(\\d+)"))){
            temp.push_back(stoi(s[0]));
            a = s.suffix().str();
        }
        tickets.push_back(temp);
    }

//part one:
    int error = 0;
    for (int i = 0; i<tickets.size(); i++){
        for (int j = 0; j<tickets[i].size(); j++){
            int trues = 0;
            for (auto const& x: rules){
                if (in_range(tickets[i][j], x.second)){
                    trues++;
                } 
            }
            if (trues == 0) {
                error += tickets[i][j];
                tickets[i][j] = -1;
            }
        }
    }
    cout << "part one: " << error << endl;

//part two:
    map<int, vector<string>> possible;
    map<int, vector<string>> seen;
    for (int i = 0; i<tickets.size(); i++){
        for (int j = 0; j<tickets[i].size(); j++){
            for (auto const& x: rules){
                if (in_range(tickets[i][j], x.second) && tickets[i][j] != -1){
                    if (!contains(possible[j], x.first) && !contains(seen[j], x.first)){
                        possible[j].push_back(x.first);
                    }
                } else if (!in_range(tickets[i][j], x.second) && tickets[i][j] != -1){
                    if (contains(possible[j], x.first)){
                        possible[j].erase(find(possible[j].begin(), possible[j].end(), x.first));
                    }
                    seen[j].push_back(x.first);
                }
            }
        }
    }


    map<int, string> column_field;
    while (!possible.empty()){
        int to_erase;
        string s_to_erase;
        for (auto const& x : possible){
            if (x.second.size() == 1){
                column_field[x.first] = x.second[0];
                to_erase = x.first;
                s_to_erase = x.second[0];
            }
        }
        possible.erase(to_erase);
        for (auto const& x : possible){
            if (find(x.second.begin(), x.second.end(), s_to_erase) != x.second.end()){
                possible[x.first].erase(find(x.second.begin(), x.second.end(), s_to_erase));
            }
        }
    }

    long long int total = 1;
    for (int i = 0; i<column_field.size(); i++){
        if (regex_match(column_field[i], regex("departure \\w+"))){
            total *= my_ticket[i];
        }
    }

    cout << "part two: " << total;

    return 0;
}